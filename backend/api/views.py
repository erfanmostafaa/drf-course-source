from blog.models import Article
from .serializers import ArtricleSerializers , UserSerializers
from rest_framework.viewsets import ModelViewSet
#from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from django.contrib.auth.models import User
from .permissions import IsSuperUserOrStaffReadOnly  ,  IsStaffOrReadOnly  , IsAuthorOrReadOnly
# Create your views here.


class ArticleViewSet(ModelViewSet):
   
    queryset = Article.objects.all()
    serializer_class = ArtricleSerializers
    def get_permissions(self):
        if self.action in ['list' ,'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [ IsStaffOrReadOnly  , IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly, )













