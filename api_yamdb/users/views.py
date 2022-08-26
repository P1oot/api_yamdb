from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserEditSerializer, AuthSerializer
from rest_framework import viewsets, permissions, status, mixins
from .permissions import Admin
from rest_framework.decorators import action
from rest_framework.response import Response
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
import smtplib


class AuthViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # create message object instance
        # msg = MIMEMultipart()
        # message = "Thank you"
        # setup the parameters of the message
        address_from = 'address@gmail.com'
        password = 'password'
        address_to = kwargs.get('email')
        message = 'bla'
        # msg['From'] = "address@gmail.com"
        # msg['To'] = kwargs.get('email')
        # msg['Subject'] = "Subscription"
        # add in the message body
        # msg.attach(MIMEText(message, 'plain'))
        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        # Login Credentials for sending the mail
        server.login(address_from, password)
        # send the message via the server.
        server.sendmail(address_from, address_to, message)
        server.quit()
        # print ("successfully sent email to %s:" % (msg['To']))
        return super().create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [Admin]

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=UserEditSerializer,
    )
    def user_own_profile(self, request):
        user = get_object_or_404(User, username=request.user)
        serializer = self.get_serializer(user, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        if request.method == 'PATCH':
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
