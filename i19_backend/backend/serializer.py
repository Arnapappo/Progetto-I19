from rest_framework import serializers
from .models import *


class TipoProdottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPortata
        fields = ['id', 'nome']


class TipoPortataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPortata
        fields = ['id', 'nome']


class ProdottoSerializer(serializers.ModelSerializer):
    tipo = serializers.IntegerField(source='tipo.id')
    tipoPortata = serializers.IntegerField(source='tipoPortata.id')

    class Meta:
        model = Prodotto
        fields = ['id', 'nome', 'descrizione', 'prezzo', 'tempoPreparazione', 'tipo', 'tipoPortata']


class ProdottoOrdinatoSerializer(serializers.ModelSerializer):
    prodotto = serializers.PrimaryKeyRelatedField(queryset=Prodotto.objects.all())
    tempoInizioLavorazione = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ProdottoOrdinato
        fields = ['id', 'idTavolo', 'quantita', 'tempoInizioLavorazione', 'prodotto', 'statoProdottoOrdinato']

    def to_representation(self, instance):
        self.fields['prodotto'] = ProdottoSerializer()
        return super(ProdottoOrdinatoSerializer, self).to_representation(instance)