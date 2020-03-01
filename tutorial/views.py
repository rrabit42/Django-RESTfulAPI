from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be views or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
"""
Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.
"""