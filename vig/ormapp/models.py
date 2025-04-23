from django.db import models
from django.contrib import admin
class movie (models.Model):
    User_id=models.CharField(max_length=20, primary_key=True)
    User_Name=models.CharField(max_length=100)
    Email_ID=models.EmailField()
    Phone_No=models.IntegerField()
    Movie_Name=models.CharField(max_length=100)   
    Show_DateTime=models.DateTimeField()
    No_of_seats=models.IntegerField( )
class MovieAdmin(admin.ModelAdmin):
    list_display=('User_id','User_Name','Email_ID','Phone_No','Movie_Name','Show_DateTime','No_of_seats')


