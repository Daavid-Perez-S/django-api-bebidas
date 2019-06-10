from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bebidas
from .serializers import BebidasSerializer

from django.shortcuts import get_object_or_404

# Create your views here.

class BebidasView(APIView):

    # Retornamos todas las bebidas existentes
    def get(self, request):
        bebidas = Bebidas.objects.all()
        # The many param informs the serializer that it will be serializing more than a single bebida.
        serializer = BebidasSerializer(bebidas, many=True)
        return Response({"bebidas": serializer.data})

    def post(self, request):
        bebida = request.data.get('bebida')

        # Create an bebida from the above data
        serializer = BebidasSerializer(data=bebida)
        if serializer.is_valid(raise_exception=True):
            bebida_saved = serializer.save()
        return Response({"success": "Bebida '{}' created successfully".format(bebida_saved.name)})

    def put(self, request, pk):
        saved_bebida = get_object_or_404(Bebidas.objects.all(), pk=pk)
        data = request.data.get('bebida')
        serializer = BebidasSerializer(instance=saved_bebida, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            bebida_saved = serializer.save()
        return Response({"success": "Bebida '{}' updated successfully".format(bebida_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        bebida = get_object_or_404(Bebidas.objects.all(), pk=pk)
        bebida.delete()
        return Response({"message": "Bebidas with id `{}` has been deleted.".format(pk)},status=204)


"""
Ejemplo para añadir una nueva bebida.

{
    "bebida":{
        "name": "nombre de algo",
        "description": "descripcion de algo",
        "image_url": "http://algo"
    }
}
"""
