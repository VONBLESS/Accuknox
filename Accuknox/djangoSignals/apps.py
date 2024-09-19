from django.apps import AppConfig


class DjangosignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoSignals'

    def ready(self):
        import djangoSignals.signals
