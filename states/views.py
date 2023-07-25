from rest_framework import generics
from .serializer import StateSerializer
from .models import State
from .permissions import IsOwnerOrReadOnly


class StateList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = State.objects.all()
    serializer_class = StateSerializer
