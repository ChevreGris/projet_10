from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from softdesk_app.models import User, Contributor, Project, Issue, Comment
from softdesk_app.serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

    
def signup_page(request):
    form = forms.SigupForm()
    if request.method == 'POST':
        form = forms.SigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    return render(request, 'softdesk_app/signup.html', context={'form': form})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('projects')
        message = 'Identifiants invalides.'
    return render(request, 'softdesk_app/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


class UsersAPIView(APIView):
    def get(self, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ProjectsAPIView(APIView):
    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_detail_project_view(request, id):

    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.methode == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_project_view(request, id):

    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.methode == "PUT":
        serializer = ProjectSerializer(project, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_NOT_REQUEST)


@api_view(['DELETE', ])
def api_delete_project_view(request, id):

    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.methode == "DELETE":
        operation = project.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
def api_create_project_view(request):

    user = request.user
    project = Project(author_user=user)

    if request.method == "POST":
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]
    #def get_queryset(self):
    #    return self.request.user.project_set.all()

'''
    def get_serializer(self):
        if self.action == 'list':
            return ProjectSerializer
        elif self.action == 'create':
            return ProjectCreateSerializer
'''