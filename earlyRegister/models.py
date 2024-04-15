from django.db import models

# Create your models here.
class EarlyRegister(models.Model):
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False, db_index=True, verbose_name='Email Address')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name