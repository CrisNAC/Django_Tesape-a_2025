from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def user_profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user_profile_list.html', {'profiles': profiles})

def main_page(request):
    return render(request, 'main_page.html')

def user_profile_detail(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    return render(request, 'user_profile_detail.html', {'profile': profile})
