from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "evolvemedicus.core"
    verbose_name = "Core"

    def ready(self):
        import evolvemedicus.core.signals

