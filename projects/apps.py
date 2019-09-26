from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'
    
    def ready(self):
        from scheduler import update
        update.start()
