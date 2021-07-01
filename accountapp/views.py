from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')  # 여기까지 아주 초 간단한 뷰가 작성된 것 #HttpResponse 대문자 잘 적어야함
