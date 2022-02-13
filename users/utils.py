from django.db.models import Q

from .models import Profile



def searchProfile(request):
    search_query= ''

    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')
    
    
    profiles= Profile.objects.distinct().filter(
        Q(name__icontains= search_query) |
        Q(username__icontains= search_query) |
        Q(short_intro__icontains= search_query) |
        Q(bio= search_query) 
        )

    return profiles , search_query