from django.shortcuts import render

def homepage(request):
    return render(request, 'core/index.html')

def profile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'core/profile.html', {'profile': profile})
