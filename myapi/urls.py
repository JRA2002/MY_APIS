from .api import ProductViewSet
from rest_framework import routers
#create routes for api
router = routers.DefaultRouter()

#register all routes and put direction , view, name
router.register('api',ProductViewSet,'api')

urlpatterns = router.urls




