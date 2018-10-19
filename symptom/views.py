from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from symptom.models import *

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

import json
import ast

#request 정의해주고, function 안에서 1번은 사용해주어야 함
#try - exception 구문으로 해야 잘 먹음

#csrf 정의해주어서 보안 관련 이슈 해결
@csrf_exempt 
def login(request):
    if request.method == 'GET':
        #깔끔하게 login info 보내주는 기능 (dict 형태로 SEND)
        try:
            result = Patient.objects.get(nickname='sample', password='samsam') #Patient 모델에서 id, pw에 맞는 객체 불러오기 성공하면 패스
            return HttpResponse('success')
        except Exception as e:
            print(str(e))
            return HttpResponse('failure')
    else:
        return HttpResponse('Wrong Request')

@csrf_exempt
def ask_question(request):
    if request.method == 'GET':
        question_one = Questions.objects.get(question_index=1) #Question에 인덱싱을 부여해서 각 질환, 혹은 질병에 맞게 Question 조합을 만들 수 있을 듯
        question_cont = question_one.question_a #불러온 객체의 세부 질문 전달 가능
        return HttpResponse(str(question_cont))
    else:
        return HttpResponse('failure')


@csrf_exempt
def testing(request):
    if request.method == 'GET':
        try:
            targetuser = Patient.objects.get(nickname='sample')
            return render(request, 'symptom/index.html', {'tar':targetuser}) #디렉토리명/.html 파일 형태로 render, {}안에 넘길 정보를 쿼리셋으로 정의해서 template으로 넘겨주고, template에서 필요한 정보 표시해주면 됨
        except Exception as e:
            print(str(e))
            return HttpResponse('Failure')
    else: 
        return HttpResponse('Wrong Request')

def ajaxtest(request):
    if request.method == 'POST':
        try:
            received_ajax = request.POST.get('data', None)
            print(received_ajax)
            ques = Questions.objects.get(q_index=1)
            return render(request, 'symptom/question.html', {'questions':ques}) #고쳐야 함
            
        except Exception as e:
            print(str(e))
            return HttpResponse('Failure')
    else: 
        return HttpResponse('Wrong Request')
            
