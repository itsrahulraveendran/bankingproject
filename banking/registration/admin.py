from django.contrib import admin
from .models import District
from .models import Branch
from .models import BankAccountApplication
from .models import Branch
from .models import BankAccountApplication
# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(BankAccountApplication)