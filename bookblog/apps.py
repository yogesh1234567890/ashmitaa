from django.apps import AppConfig


class BookblogConfig(AppConfig):
    name = 'bookblog'


    def ready(self):
        import bookblog.signals
