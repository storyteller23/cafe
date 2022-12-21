from django import forms
from .models import Order, Employee, Position

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client_name', 'dishes', 'served_employee', 'total_price')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['served_employee'].queryset = Employee.objects.filter(position__server=True)
