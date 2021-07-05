from django.shortcuts import render
from .models import Student #Import model class name
# from django.http import HttpResponse,JsonResponse # use for View model
from .serializers import StudentSerializer #Import serializer class name
from rest_framework.renderers import JSONRenderer # user of data JSON format Delver

# Create your views here.
def Student_details(request,pk):
    stu=Student.object.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render (serializer.data)
    return HttpResponse(json_data,content_type='Application/json')