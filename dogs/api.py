from rest_framework import serializers, viewsets

from .models import Dogs_Owner

class DogsOwnerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Dogs_Owner
        fields = ('name', 'description', 'weight', 'breed', 'friendly')

class DogsOwnerViewset(viewsets.ModelViewSet):
    serializer_class = DogsOwnerSerializer
    queryset = Dogs_Owner.objects.all()