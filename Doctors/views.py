from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from .models import Doctor
from .serializers import DoctorSerializer

@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_doctor(request):
    query_params = request.query_params

    name = query_params.get('name')
    specialty = query_params.get('specialty')
    organization = query_params.get('organization')

    q_obj = Q()

    if name:
        q_obj |= Q(name__icontains=name)
    if specialty:
        q_obj |= Q(specialty__icontains=specialty)
    if organization:
        q_obj |= Q(organization__icontains=organization)

    doctors = Doctor.objects.filter(q_obj)

    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=404)

    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])  
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
