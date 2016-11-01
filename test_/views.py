from django.http import HttpResponse


def login_required(request):
    if 'user' in dir(request):
        if request.user.is_authenticated():
            return HttpResponse('success')
    return HttpResponse('fail')


def blank(request):
    return HttpResponse('')
