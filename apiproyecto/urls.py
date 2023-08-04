from rest_framework.routers import SimpleRouter
from .api import AlumnosViewSet, PersonalViewSet, PeriodosEscolaresViewSet, CarrerasViewSet

router = SimpleRouter()
router.register(r'api/Alumnos', AlumnosViewSet, 'Alumnos')
router.register('api/Personal', PersonalViewSet, 'Personal')
router.register('api/Carreras', CarrerasViewSet, 'Carreras')
router.register('api/PeriodosEscolares', PeriodosEscolaresViewSet, 'PeriodosEscolares')

# combinar las URLs generadas por el enrutador con otras URLs definidas manualmente en una única lista
urlpatterns = [
    *router.urls,
]
