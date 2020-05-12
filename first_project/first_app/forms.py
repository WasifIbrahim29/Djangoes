from django import forms

class TestForm(forms.Form):
    text = forms.CharField(min_length=7) 
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10)
    email = forms.EmailField()

    def clean_integer(self):
        integer= self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer