from django.urls import path,include
from  rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'personajes', views.PersonajesViewSet)
router.register(r'peliculas', views.PeliculasViewSet)
router.register(r'planetas', views.PlanetasViewSet)
router.register(r'especies', views.EspeciesViewSet)
router.register(r'swapi', views.SWAPIViewSet, basename='swapi')
router.register(r'swapiplenetas', views.SWAPIPlanetasViewSet, basename='swapiplanetas')
router.register(r'swapipeliculas', views.SWAPIPlanetasViewSet, basename='swapipeliculas')
router.register(r'swapiespecies', views.SWAPIEspeciesViewSet, basename='swapiespecies')

urlpatterns = [
    path('', include(router.urls))
]