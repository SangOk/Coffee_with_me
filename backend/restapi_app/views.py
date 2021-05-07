from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
