from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from guardian.mixins import GuardianUserMixin
from datetime import datetime, date, timedelta
import pytz
from django.utils import timezone
from django.db.models import Q
from django_resized import ResizedImageField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_pics/user_{0}/{1}'.format(instance.id, filename)


class User(GuardianUserMixin, AbstractUser):
    passchanged = models.NullBooleanField(default=False)
    picture = ResizedImageField(size=[800, 480], upload_to=user_directory_path, blank=True, null=True)

    @property
    def profile(self):
        if hasattr(self, "superadmin"):
            return self.superadmin
        elif hasattr(self, "officer"):
            return self.officer
        elif hasattr(self, "admin"):
            return self.admin
        else:
            return self

    @property
    def is_admin(self):
        return hasattr(self, "admin")

    @property
    def is_superadmin(self):
        return hasattr(self, "superadmin")

    @property
    def is_officer(self):
        return hasattr(self, "officer")


    class Meta(AbstractUser.Meta):
        permissions = (
            ("access_admin_pages", "Access Admin pages"),
            ("access_superadmin_pages", "Access superadmin pages"),
            ("access_officer_pages", "Access officer pages"),
        )


class Profile(models.Model):
    gender_type = (
        ('F', _("Female")),
        ('M', _("Male")),
        ('U', _("Undisclosed")),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=True, null=True)
    dateadd = models.DateField(blank=True, null=True, default=datetime.now(tz=pytz.UTC))
    gender = models.CharField(max_length=1, choices=gender_type, null=True)

    def __str__(self):
        if self.user.first_name:
            return "{}.{}".format(self.user.first_name[0], self.user.last_name)
        return self.user.username

    class Meta:
        abstract = True


class Admin(Profile):
    allow_comments = models.BooleanField(default=True)

    class Meta(Profile.Meta):
        verbose_name = "Admin"
        verbose_name_plural = "Admin"


class Superadmin(Profile):
    allow_comments = models.BooleanField(default=True)

    class Meta(Profile.Meta):
        verbose_name = "Superadmin"
        verbose_name_plural = "Superadmin"

    # @property
    # def average_score(self):
    #     reviews = self.review_set.all()
    #     score = reviews.aggregate(models.Avg("score"))["score__avg"]
    #     return score


class Officer(Profile):
    active = models.NullBooleanField(default=True)

    class Meta(Profile.Meta):
        verbose_name = "Officer"
        verbose_name_plural = "Officer"


# class LoggedInUser(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="logged_in_user", on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=32, blank=True, null=True)
#     # academicyear = models.ForeignKey(Student, on_delete=models.PROTECT, blank=True, null=True)
#     # studentpk = models.ForeignKey(Academicyear, on_delete=models.PROTECT, blank=True, null=True)
#
#     def __str__(self):
#         return self.user.first_name
