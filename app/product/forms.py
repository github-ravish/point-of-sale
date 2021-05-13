from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Column, Row
from crispy_forms.bootstrap import AppendedText

from .models.product import Product


class ProductModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field(AppendedText(
                'slug', '<span onclick="startScanner()" class="material-icons material-icons-outlined password-toggle">qr_code</span>')),
            'name',
            'quantity',
            'cost_price',
            'selling_price',
        )
        self.fields['slug'].label = "Product ID"

    class Meta:
        model = Product
        fields = ['slug', 'name', 'quantity', 'cost_price', 'selling_price']
