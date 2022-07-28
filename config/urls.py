
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog
from hifuji.profiles.views import ProfileView

admin.autodiscover()

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # path("accounts/", include("allauth.urls")),
    # path("accounts/profile/", ProfileView.as_view()),
    # path("profiles/", include("hifuji.profiles.urls", namespace="profiles")),
    # path("core/", include("hifuji.core.urls", namespace="core")),
    path("", RedirectView.as_view(pattern_name="core:dashboard")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [path("rosetta/", include("rosetta.urls"))]
