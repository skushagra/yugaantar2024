from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from earlyRegister.models import EarlyRegister
# Create your views here.

class HomeView(View):

    def get(self, request):
        if(request.user.is_authenticated):
            earlyUsers = len(list(EarlyRegister.objects.all()))
            return render(request, 'home.html', {
                'earlyUsers': earlyUsers
            })
        else:
            return render(request, 'login.html')


class EarlyRegisterView(View):

    def get(self, request):
        earlies = EarlyRegister.objects.all()
        return render(request, 'earlyregister.html', {
            'earlies': earlies
        })

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': 200,
                'message': 'Login successful!'
            })
        else:
            return JsonResponse({
                'status': 401,
                'message': 'Login failed. Please try again.'
            })


class BackendUnAccessibaleView(View):
    
        def get(self, request):
            return JsonResponse({
                'status': 503,
                'message': 'Backend is not accessible at the moment. Please try again later.'
            })