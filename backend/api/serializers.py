from rest_framework import serializers 
from blog.models import Article
from django.contrib.auth import get_user_model

class ArtricleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id" ,"titile","slug", "author" , "content" ,"publish",  "status" , "updated", "created")




class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"