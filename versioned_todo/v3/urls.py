from .api import TodoViewSetCustom
from rest_framework import routers

router_v3 = routers.DefaultRouter()
router_v3.register(r'todo3', TodoViewSetCustom, 'todosCustom3')

urlpatterns = router_v3.urls