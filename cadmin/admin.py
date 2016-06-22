from django.contrib import admin
from .models import Client
from .models import Product
from .models import Request
from .models import Status
from .models import Company

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Request)
admin.site.register(Status)
admin.site.register(Company)
