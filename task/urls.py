from rest_framework import routers
from task.views import TaskViewSet

router = routers.SimpleRouter()
router.register('', TaskViewSet)
urlpatterns = router.urls
