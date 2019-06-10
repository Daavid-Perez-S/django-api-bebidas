from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Bebidas
from .serializers import BebidasSerializer

from django.shortcuts import get_object_or_404

# Create your views here.

class BebidasView(ListCreateAPIView):

    queryset = Bebidas.objects.all()
    serializer_class = BebidasSerializer

    # Los métodos get y post ya están dentro de listapiview y createapiview.

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


class SingleBebidasView(RetrieveUpdateDestroyAPIView):
    queryset = Bebidas.objects.all()
    serializer_class = BebidasSerializer


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
