from django.contrib import admin
from .models import Usuario
from .models import Vehiculo
from .models import Ventas

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, 			{'fields': ['password']}),
    ('Informacion', {'fields': ('nombre','fechaNacimiento','apellido1','apellido2','correo','telefono')}),
    ]
    list_display = ('nombre','apellido1','fechaNacimiento','correo')
    list_filter = ['fechaNacimiento']
admin.site.register(Usuario, UsuarioAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    fields = ['precio','modelo', 'version', 'motor']
    list_display = ('precio','modelo','version','motor')
    list_filter = ['modelo']
admin.site.register(Vehiculo, VehiculoAdmin)

class VentasAdmin(admin.ModelAdmin):
   fields = ['usuario','vehiculo','precioTotal']
admin.site.register(Ventas, VentasAdmin)
#Register your models here.