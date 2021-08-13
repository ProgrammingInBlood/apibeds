from django import forms
from .models import Add_new_product
#DataFlair
class Add_new_product_form(forms.ModelForm):
    class Meta:
        model = Add_new_product
        fields = '__all__'