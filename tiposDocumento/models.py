from django.db import models

# Create your models here.
class TiposDocumento(models.Model):
    idTypeDoc           =   models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    description         =   models.CharField(max_length=30)
