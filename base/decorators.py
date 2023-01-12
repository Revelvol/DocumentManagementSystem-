from django.http.response import HttpResponse
from django.shortcuts import redirect


def unauthenthicatedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        # masukin function disini
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return wrapper_func


def allowedUsers(*allowed_roles):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # masukin function disini
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponse("you are not admins ")  # nanti ini diganti aja
        return wrapper_func

    return decorator
