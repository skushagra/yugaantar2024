from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from django.views.decorators.csrf import csrf_exempt
from .models import EarlyRegister
import re
import csv

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RegisterEarlyUserView(View):

    # @method_decorator(ratelimit(key='ip', rate='10/s'))
    def get(self, request):
        early_users = EarlyRegister.objects.count()
        return JsonResponse({
            'total_early_users': early_users
        })
    
    # @method_decorator(ratelimit(key='ip', rate='10/s'))
    def post(self, request):
        try:
            user_mail = request.POST.get('email')
            print(user_mail)
            if not user_mail:
                raise RuntimeError('Email cannot be empty. No user to register. Hence ignored.')
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user_mail):
                raise RuntimeError('Submitted string is not a valid email address. Hence igonred.')
            user = EarlyRegister.objects.filter(email=user_mail)
            if user.exists():
                raise RuntimeError('Early registration already exists for this email address. Hence ignored.')
            user = EarlyRegister(email=user_mail)
            user.save()
        except Exception as e:
            return JsonResponse({
                'message': str(e)
            })
        return JsonResponse({
                'message': 'Early registration successful. Thank you!'
            })


class ExportEarlyRegisterView(View):

    def get(self, request):
        
        if not request.user.is_authenticated:
            return JsonResponse({
                'message': 'Access not allowed at this level(0)'
            })
        early_users =  EarlyRegister.objects.all().values_list('email', flat=True)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="earlyUsers.csv"'

        writer = csv.writer(response)
        for email in early_users:
            writer.writerow([email])

        return response