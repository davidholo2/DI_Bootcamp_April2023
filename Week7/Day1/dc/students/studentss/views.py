from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    date_joined_param = request.GET.get('date_joined')

    if date_joined_param:
        students = Student.objects.filter(date_joined=date_joined_param)
    else:
        students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=204)
