from django import forms
from assets.models.models_assets import Assetstable


class AssetsForm(forms.ModelForm):
    class Meta:
        model = Assetstable
        fields = ['nameconfig', 'coin', 'sell', 'buy', 'timer']