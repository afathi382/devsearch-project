from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile




def createprofile(sender, instance, created, **kwargs):
    if created:
        user= instance
        profile= Profile.objects.create(
            user= user,
            username= user.username,
            email=  user.email,
            name= user.first_name
        )


post_save.connect(createprofile , User)



def deleteuser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_delete.connect(deleteuser , Profile)