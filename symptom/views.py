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

@csrf_exempt
def splash(request):
    return render(request, 'symptom/splash.html', {})

@csrf_exempt
def login_show(request):
    return render(request, 'symptom/login.html', {})

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        try:
            received_id = request.POST.get('id', None)
            received_password = request.POST.get('password', None)
            auth_result = Patient.objects.get(username=received_id, password=received_password)
            return HttpResponse('Success')

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')
    else:
        return HttpResponse('Not POST')
    
def show_main(request):
    return render(request, 'symptom/main.html')

def show_signup(request):
    return render(request, 'symptom/signup.html')

def register_new(request):
    if request.method == 'POST':
        try:
            received_username = request.POST.get('signup_id', None)
            received_password = request.POST.get('signup_password', None)
            received_email = request.POST.get('signup_email', None)
            received_sex = request.POST.get('signup_sex', None)
            received_age = request.POST.get('signup_age', None)

            temp_patient = Patient.objects.filter(username=received_username)
            
            if not temp_patient.exists():
                try:
                    new_regist_info = Patient(username=received_username,
                                                password=received_password,
                                                email=received_email,
                                                sex=received_sex,
                                                age=received_age)
                    new_regist_info.save()
                    return HttpResponse('Success')

                except Exception as e:
                    print(str(e))
                    return HttpResponse('Register fail')

            return HttpResponse('success')

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not POST')

@csrf_exempt
def check_eye(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='눈')
            tmp_index = Logdata(cate='eye', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_head(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='머리')
            tmp_index = Logdata(cate='head', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_nose(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='코, 귀')
            tmp_index = Logdata(cate='nose', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_mouth(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='입, 목')
            tmp_index = Logdata(cate='mouth', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_muscle(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='근육')
            tmp_index = Logdata(cate='muscle', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_skin(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='피부')
            tmp_index = Logdata(cate='skin', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_digest(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='소화')
            tmp_index = Logdata(cate='digest', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_ankle(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='관절')
            tmp_index = Logdata(cate='ankle', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def check_reproduct(request):
    if request.method == 'GET':
        try:
            bodypart_data = Bodypart.objects.get(partname='생식기관')
            tmp_index = Logdata(cate='reproduct', tmp=0)
            tmp_index.save()
            return render(request, 'symptom/check_symptom.html', {'body' : bodypart_data}) #Data는 여기서 넘김 (href)

        except Exception as e:
            print(str(e))
            return HttpResponse('Wrong Request')

    else:
        return HttpResponse('Not the Human')

@csrf_exempt
def answer(request):
    if request.method == 'GET':
        try:
            int_a = int(request.GET.get('ans_a'))
            int_b = int(request.GET.get('ans_b'))
            int_c = int(request.GET.get('ans_c'))
            int_d = int(request.GET .get('ans_d'))
            
            input_list = [int_a, int_b, int_c, int_d]

            temporary = Logdata.objects.get(tmp=0)

            eye_list = ['건조/눈물', '야맹증', '각막, 결막, 망막', '다래끼']
            head_list = ['두통', '어지러움', '빈혈', '피로']
            nose_list = ['감기', '비염', '코피', '이명']
            mouse_list = ['치아, 잇몸', '가래', '입질환', '입술']
            muscle_list = ['근육통', '골격근장애', '접질림, 삠, 인대', '외상 및 좌상']
            skin_list = ['피부염', '고름, 딱지', '모낭염', '종기']
            digest_list = ['배땡김', '소화불량, 과식', '체함', '구역, 구토']
            reproduct_list = ['월경 통증', '생리통', '월경전증후군', '월경불순']

            if temporary.cate == 'eye':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del eye_list[i]
                        i = i+1
                '''
                global queryset
                queryset = Medicine.objects.filter(effect__contains='안구')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'head':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del head_list[i]
                        i = i+1
                '''
                queryset = Medicine.objects.filter(effect__contains='두통')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'nose':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del nose_list[i]
                        i = i+1 
                '''
                queryset = Medicine.objects.filter(effect__contains='감기')
                temporary.delete()
                print(queryset)
                print(len(queryset))


            if temporary.cate == 'mouse':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del mouse_list[i]
                        i = i+1  
                '''
                queryset = Medicine.objects.filter(effect__contains='입술')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'muscle':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del muscle_list[i]
                        i = i+1   
                '''
                queryset = Medicine.objects.filter(effect__contains='근육')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'skin':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del skin_list[i]
                        i = i+1 
                '''
                queryset = Medicine.objects.filter(effect__contains='피부')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'digest':
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del digest_list[i]
                        i = i+1   
                '''
                queryset = Medicine.objects.filter(effect__contains='배')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            if temporary.cate == 'reproduct': 
                '''
                i = 0
                for li in input_list:
                    if li == 1:
                        del reproduct_list[i]
                        i = i+1
                '''
                queryset = Medicine.objects.filter(effect__contains='두통')
                temporary.delete()
                print(queryset)
                print(len(queryset))

            return render(request, 'symptom/result.html', {'med':queryset})

        except Exception as e:
            print(str(e))
            return HttpResponse('Failure')
    else: 
        return HttpResponse('Wrong Access')

@csrf_exempt
def result(request):
    return render(request, 'symptom/result.html', {'med': queryset })