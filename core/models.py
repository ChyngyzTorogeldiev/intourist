from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE,
        related_name='profile'
	)
	region = models.CharField(max_length=1, choices=(
    	('B', 'Bishkek'),
    	('C', 'Chuy'),
    	('I', 'Yssyk - Kol'),
    	('N', 'Naryn'),
    	('T', 'Talas'),
    	('O', 'Osh'),
    	('J', 'Jalal-Abad'),
    	('A', 'Batken'),
	))
 	photo = models.ImageField(
        upload_to='profile_photo',
        null=True, blank=True
	)

 	def __str__(self):
		return self.user.username
