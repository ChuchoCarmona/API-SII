from apiproyecto.models import Alumnos, Carreras, PeriodosEscolares, Personal
from rest_framework import viewsets, permissions
from .serializers import AlumnosSerializers, PersonalSerializers, PeriodosEscolaresSerializers, CarrerasSerializers
from rest_framework import status
from rest_framework.response import Response

class AlumnosViewSet(viewsets.ModelViewSet):
    # Se especifica que no se requiere autenticación o permisos específicos
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        # Obtener los valores de 'no_de_control' y 'nip' de los parámetros de consulta (query parameters) de la solicitud GET
        no_de_control = request.query_params.get('no_de_control')
        nip = request.query_params.get('nip')

        # Verificar si se proporcionan los valores de 'no_de_control' y 'nip'
        if no_de_control is None or nip is None:
            error_message = "Falta el parámetro 'no_de_control' y/o 'nip'."
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        # Intentar obtener una queryset filtrando los objetos 'Alumnos' que coincidan con los valores proporcionados
        queryset = Alumnos.objects.filter(no_de_control=no_de_control, nip=nip)

        # Verificar si la queryset está vacía
        if not queryset.exists():
            error_message = "El alumno no existe."
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        # Serializar y devolver los resultados con serializador generico
        # serializer = self.serializer_class(queryset, many=True)
        #enviar los datos del serializador de zaida para mostrarlos correctamente en el reponse
        serializer = AlumnosSerializers(queryset, many=True)
        return Response(serializer.data)


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonalSerializers

class PeriodosEscolaresViewSet(viewsets.ModelViewSet):
    queryset = PeriodosEscolares.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeriodosEscolaresSerializers

class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarrerasSerializers