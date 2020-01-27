from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('hello brother')

def convert_dates(dates):
    #function that gets the weekly news_of_day
    day_number=dt.date.weekday(dates)
     days=['Monday','Tuesday','Wednesday','Thursday','Saturday',"Sunday"]    

def news_of_day(request):
    date=dt.date.today()
    html=f'''
            <html>
               <body>
                   <h1>{date.day}-{date.month}-{date.year}</h1>
            </html>
                '''
    return HttpResponse(html)
