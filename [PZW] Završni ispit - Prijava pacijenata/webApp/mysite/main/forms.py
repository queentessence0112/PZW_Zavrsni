from django import forms
from .models import Pacijent


class PacijentForm(forms.ModelForm):

    class Meta:
        model = Pacijent
        fields = ('broj_zdravstvene','ime_pacijenta','prezime_pacijenta','broj_mobitela', 'razlog_dolaska', 'odjel')


    def __init__(self, *args, **kwargs):
        super(PacijentForm,self).__init__(*args, **kwargs)
        self.fields['odjel'].empty_label = "Odaberite"