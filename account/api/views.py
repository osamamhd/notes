from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer


@api_view(['POST', ])
def create_new_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {
                'response': 'user is registered successfully',
                'email': account.email,
                'token': Token.objects.get(user=account).key,
            }
            return Response(data=data)
        return Response(serializer.errors)