# from django.db import models
# from django.db.models import Model
# # Create your models here.
#
# class Bankform(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     age = models.IntegerField()
#     gender = models.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(widget=models.Textarea)
#     district = models.ChoiceField(choices=[('Ernakulam', 'Ernakulam'), ('Alappuzha', 'Alappuzha')])  # Add more choices
#     branch = models.ChoiceField(choices=[('Aluva', 'Aluva'), ('Edapally', 'Edapally')])  # Add more choices
#     account_type = models.ChoiceField(
#         choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')])  # Add more choices
#     materials_provided = models.MultipleChoiceField(
#         choices=[('debit-card', 'Debit Card'), ('credit-card', 'Credit Card'), ('cheque-book', 'Cheque Book')],
#         widget=models.CheckboxSelectMultiple,
#         required=False  # Remove this if at least one material is required
#     )
# models.py
from django.db import models
from django.db.models import Model

class District(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class BankAccountApplication(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    materials_provided = models.TextField()

    def __str__(self):
        return self.name

