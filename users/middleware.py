# users/middleware.py
from django.shortcuts import redirect

class RoleSubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split('.')[0]  # get subdomain
        if request.user.is_authenticated:
            if host == 'student' and request.user.role != 'student':
                return redirect('login')
            elif host == 'instructor' and request.user.role != 'instructor':
                return redirect('login')
            elif host == 'admin' and request.user.role != 'admin':
                return redirect('login')
        return self.get_response(request)
