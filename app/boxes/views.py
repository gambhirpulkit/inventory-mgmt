from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Boxes
from .serializers import BoxSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Boxes.objects.all()
    serializer_class = BoxSerializer

@login_required
def add_box(request):
    return HttpResponse("hey")