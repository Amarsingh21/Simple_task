from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    school=serializers.CharField(max_length=100)
    address=serializers.CharField(max_length=150)
    rollno=serializers.IntegerField()
    Mobileno=serializers.IntegerField()
    email=serializers.EmailField(max_length=50)