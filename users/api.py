from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from twilio.rest import Client
import random

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_throttles(self):
        if self.action == "update":
            # aca vamos a decir que use el throttle_scope
            self.throttle_scope = "generate_code" 
        return super().get_throttles()

    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        code = random.randint(1000, 9999)
        # si queremos aumentar datos al request primero debemos hacerlo mutable
        request.data._mutable = True
        request.data["code"] = code
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            # twilio credentials
            account_sid = 'AC4528f32992adfbeed6cada2a919596b8'
            auth_token = 'c08a37b18dc5a1b6ff6f8199374db4ea'
            client = Client(account_sid, auth_token)

            client.messages.create(
                from_='+13208184989',
                body=f'Hola tu código es {code}',
                to='+51947238341'
            )
            
            serializer.save()
            return Response({
                "ok": True,
                "message": "user update"
            })



class UserViewGenericViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def retrieve(self, request, *args, **kwards):    #para hacer referencia al mixin
        return super().retrieve(request, *args, **kwards)
    
