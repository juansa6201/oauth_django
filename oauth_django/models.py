from django.db import models
from django.conf import settings

# Create your models here.

class Mensaje(models.Model):
    mensaje = models.CharField('Texto', max_length = 180)
    datetime = models.DateTimeField('Fecha', auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= True)
    user.verbose_name = 'Usuario'

    def __str__(self):
        return 'Mensaje nro {} - por {}'.format(self.id, self.user)

