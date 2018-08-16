from django.conf.urls import url, include
from rest_framework import routers
from main.serializer import views

router = routers.DefaultRouter()
router.register(r'bets', views.BetViewSet)
router.register(r'bet_statuses', views.BetStatusViewSet)
router.register(r'managers', views.ManagerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]