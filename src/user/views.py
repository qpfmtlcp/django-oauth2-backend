from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import User
from .serializers import SignUpSerializer, UserSerializer


class SignUpView(CreateAPIView):
    queryset = User
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
