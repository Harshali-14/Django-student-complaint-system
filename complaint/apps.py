from django.apps import AppConfig
from django.contrib.auth.models import User


class ComplaintConfig(AppConfig):
    name = 'complaint'

def create_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="harshu14"
        )