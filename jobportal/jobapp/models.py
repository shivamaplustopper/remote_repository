from django.db import models

#Registration Model Starts

class Registration_model(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=50)
    mobileno = models.BigIntegerField()
    password = models.CharField(max_length=20)

#Registration Model Ends

# Jobs Model Starts
class Banglore_model(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    domain = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)

class Hyderabad_model(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    domain = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)

class Pune_model(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    domain = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)

class Chennai_model(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    domain = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)

# Jobs Model Ends
