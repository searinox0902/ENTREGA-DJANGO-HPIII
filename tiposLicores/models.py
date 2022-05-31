from django.db import models

# Create your models here.
class TiposLicores(models.Model):
    idTypeDrink     = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name            = models.CharField(max_length=30)
