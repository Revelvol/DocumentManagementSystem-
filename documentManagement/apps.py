from django.apps import AppConfig


class DocumentmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'documentManagement'
    def ready(self):
        import documentManagement.signals
