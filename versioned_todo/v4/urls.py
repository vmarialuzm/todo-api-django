from .api import TodoViewSet
from rest_framework import routers

router_v4 = routers.DefaultRouter()
router_v4.register(r'todo4', TodoViewSet, 'todosCustom4')

urlpatterns = router_v4.urls