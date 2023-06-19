from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Department, Employee, Task, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, TaskSerializer, ProjectSerializer


class DepartmentListAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProjectRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
