#-*- coding: utf-8 -*-

from django.db import models

class Patient(models.Model):
    username = models.CharField(max_length=30, default='Null Name')
    email = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False, null=False, default=20)
    sex = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.username)

class Bodypart(models.Model):
    partname = models.CharField(max_length=100, blank=True)
    ques_a = models.CharField(max_length=100, blank=True)
    ques_b = models.CharField(max_length=100, blank=True)
    ques_c = models.CharField(max_length=100, blank=True)
    ques_d = models.CharField(max_length=100, blank=True)    
    ques_e = models.CharField(max_length=100, blank=True)
    ques_f = models.CharField(max_length=100, blank=True)
    ques_g = models.CharField(max_length=100, blank=True)
    ques_h = models.CharField(max_length=100, blank=True)
    ques_i = models.CharField(max_length=100, blank=True)
    ques_j = models.CharField(max_length=100, blank=True)
    ques_k = models.CharField(max_length=100, blank=True)
    ques_l = models.CharField(max_length=100, blank=True)
    ques_m = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.partname)

class Medicine(models.Model):
    medicineindex = models.IntegerField(blank=True)
    medicinename = models.CharField(max_length=500, blank=True)
    medicinesymptom = models.CharField(max_length=500, blank=True)
    form = models.CharField(max_length=500, blank=True)
    amount = models.CharField(max_length=500, blank=True)
    effect = models.CharField(max_length=500, blank=True)
    rating = models.IntegerField(blank=False, default=3)
    review_a = models.CharField(max_length=1000, blank=True)
    review_b = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.medicinename)

class Logdata(models.Model):
    cate = models.CharField(max_length=100, blank=True)
    log = models.CharField(max_length=500, blank=True)
    tmp = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.tmp)