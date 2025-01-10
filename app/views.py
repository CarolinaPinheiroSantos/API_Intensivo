from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class SpellAPIViews(views.APIView):
    #Post -> cadastrar dados na API
    def post(self, request):
        #Armazenar os dados que estao em JASON
        spellJson = request.data
        
        #Transformando JSON em python
        spellSerialized = SpellSerializer(data=spellJson)
        
        #verificar se os dados estao corretos
        spellSerialized.is_valid(raise_exception=True)
        
        #Salvar os dados estão corretos
        spellSerialized.save()
        
        #Retorna para o cliente o resultado da requisição
        return Response(status=201, data=spellSerialized.data)
       