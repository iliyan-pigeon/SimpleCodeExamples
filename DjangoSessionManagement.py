from django.http import HttpResponse

def set_session(request):
    request.session['username'] = 'user1'
    return HttpResponse('Session set')

def get_session(request):
    username = request.session.get('username', 'Session not set')
    return HttpResponse(username)
