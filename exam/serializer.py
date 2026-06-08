from rest_framework.serializers import ModelSerializer
from .models import Stud_Info

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Stud_Info
        fields = '__all__'