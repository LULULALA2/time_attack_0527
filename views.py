from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel
import hashlib


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if bool(email.find("@")) != True :
            return HttpResponse('이메일 형식 에러')

        if password.length >= 8:
            return HttpResponse('비밀번호 길이가 짧습니다')
        else:
            new_user = UserModel()
            new_user.email = email
            new_user.password = pwhash
            # new_user.save()
        return HttpResponse('회원가입 완료')

