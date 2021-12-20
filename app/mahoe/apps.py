from django.apps import AppConfig


class MahoeappConfig(AppConfig):
    name = 'mahoe'

    def ready(self):
        from . import signals
