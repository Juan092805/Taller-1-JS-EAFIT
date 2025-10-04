from django import forms
from .models import Search, Category

class ProductForm(forms.ModelForm):
    category_fk = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Categoría (normalizada)",
        help_text="Selecciona una categoría. Si no existe, primero créala en el admin."
    )

    class Meta:
        model = Search
        fields = ["name", "category_fk", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nombre del producto"}),
            "price": forms.NumberInput(attrs={"step": "0.01"}),
        }
