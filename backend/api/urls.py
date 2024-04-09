from django.urls import path , include
from .views import ArticleViewSet , UserViewSet
from rest_framework import routers

app_name = "api"


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', ArticleViewSet)


#urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls)),
]