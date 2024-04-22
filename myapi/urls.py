from rest_framework import routers
from .api import ProductViewset

#create routes for api
router = routers.DefaultRouter()

#register all routes and put direction , view, name
router.register('api',ProductViewset,'api')

urlpatterns = router.urls