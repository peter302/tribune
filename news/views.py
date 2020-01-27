from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
#def welcome(request):
    #return HttpResponse('hello brother')

#def convert_dates(dates):
    #function that gets the weekly news_of_day
    #day_number=dt.date.weekday(dates)
    #days=['Monday','Tuesday','Wednesday','Thursday','Saturday',"Sunday"]
    #returning the actual day of the weekly
    #day=days[day_number]

    #return day

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})



def past_days_news(request,past_date):
          try:
             # Converts data from the string Url
             date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

          except ValueError:
            # Raise 404 error when ValueError is thrown
            raise Http404()
            assert False

          if date == dt.date.today():
            return redirect(news_of_day)

          return render(request, 'all-news/past-news.html', {"date": date})


def welcome(request):
    return render(request,'welcome.html')
