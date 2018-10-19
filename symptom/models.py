#-*- coding: utf-8 -*-

from django.db import models

# 가입자 DB모델

class Patient(models.Model):
    nickname = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False, null=False, default=20)

    # 나중에 질병 예상 징후 추가해놓기
    symptom_list = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.nickname)

class Questions(models.Model):
    q_index = models.IntegerField(blank=False, null=False, default=0)
    q_a = models.CharField(max_length=50, blank=False)
    q_b = models.CharField(max_length=50, blank=False)
    q_c = models.CharField(max_length=50, blank=False)
    q_d = models.CharField(max_length=50, blank=False)
    q_e = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.question_index)
    

