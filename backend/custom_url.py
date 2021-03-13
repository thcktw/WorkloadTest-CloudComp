from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

# from djoser import views
from backend import custom

router = DefaultRouter()
router.register("users", custom.UserViewSet)

User = get_user_model()

urlpatterns = router.urls