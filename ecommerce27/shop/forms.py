from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        # Fetching all fields from Product table which is created in model file
        model=Product

        # This includes all fields from the Product model in the form
        # fields='__all__'

        # Only include the fields you need
        fields = ['id', 'name', 'desc', 'price', 'categ_id', 'image', 'stock_qty']
        # To add label, field type, attributes, placeholder etc
        widgets={
            # Set Product table fields to Model form fields
            'name': forms.TextInput(attrs={'class':'form_control', 'placeholder':"Product Name"}),
            'desc': forms.Textarea(attrs={'class':'form_control', 'placeholder':"Description"}),
            'price': forms.NumberInput(attrs={'class':'form_control', 'placeholder':"Price"}),
            'categ_id': forms.Select(attrs={'class': 'form_control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form_control', 'placeholder':"Upload Image"}),
            # 'availability': forms.BooleanInput(attrs={'class':'form_control', 'placeholder':"Availability"}),
            'stock_qty': forms.NumberInput(attrs={'class':'form_control', 'placeholder':"Stock Quantity"})
        }