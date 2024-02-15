from django.contrib.auth.models import AbstractUser, User
from apps.send_email import task_send_email
from django.db.models import Model, CharField, ImageField, TextField



class People(Model):
    image = ImageField(upload_to='workers/images/', default='workers/images/default.jpg')
    username = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    titles = TextField(null=True, blank=True)
    email = CharField(max_length=255)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        emails: list = People.objects.values_list('email', flat=True)
        task_send_email.delay("Yangi Habar", self.last_name, list(emails))




