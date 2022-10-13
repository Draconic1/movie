from django.contrib import admin

# Register your models here.
from .models import Films
from .models import Users
from .models import Seats
from .models import Orders

admin.site.register(Films)
admin.site.register(Users)
admin.site.register(Seats)
admin.site.register(Orders)