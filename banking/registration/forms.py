# from django import forms
# class Bankform(forms.Form):
#     name = forms.CharField(max_length=100)
#     dob = forms.DateField()
#     age = forms.IntegerField()
#     gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
#     phone = forms.CharField(max_length=15)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea)
#     district = forms.ChoiceField(choices=[('Ernakulam', 'Ernakulam'), ('Alappuzha', 'Alappuzha')])  # Add more choices
#     branch = forms.ChoiceField(choices=[('Aluva', 'Aluva'), ('Edapally', 'Edapally')])  # Add more choices
#     account_type = forms.ChoiceField(
#         choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')])  # Add more choices
#     materials_provided = forms.MultipleChoiceField(
#         choices=[('debit-card', 'Debit Card'), ('credit-card', 'Credit Card'), ('cheque-book', 'Cheque Book')],
#         widget=forms.CheckboxSelectMultiple,
#         required=False  # Remove this if at least one material is required
#     )
#
# forms.py
from django import forms
from .models import BankAccountApplication

class BankAccountApplicationForm(forms.ModelForm):
    class Meta:
        model = BankAccountApplication
        fields = '__all__'