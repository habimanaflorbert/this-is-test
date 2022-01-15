from home.models import *
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string
from django.core import serializers
# Create your views here.


def some_view(request):
    students = Information.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'speed', 'Time', 'Date', 'distance', 'description'])
    studs = students.values_list(
        'id', 'speed', 'time', 'date', 'distance', 'description')
    for std in studs:
        writer.writerow(std)
    return response


def my_serialize(request):
    queryset = Information.objects.all()
    queryset = serializers.serialize("xml", queryset)
    return HttpResponse(queryset, content_type="application/xml")


def index(request):
    queryset=Information.objects.all()
    if request.method == 'POST':
        speed = request.POST['speed']
        time = request.POST['time']
        date = request.POST['date']
        distance = request.POST['distance']
        desc = request.POST['desc']
        Information.objects.create(
            speed=speed, time=time, date=date, distance=distance, description=desc).save()
        message="added successfuly"
        return render(request, "index.html",{'msg':message,"query":queryset})
    return render(request, "index.html",{"query":queryset})
