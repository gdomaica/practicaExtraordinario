from django import forms

from .models import oficina, empleado


class fromularioOficina(forms.Form):
    class Meta:
        model = oficina
        fields = '__all__'

class fromularioEmpleado(forms.Form):
    class Meta:
        model = empleado
        fields = '__all__'
        