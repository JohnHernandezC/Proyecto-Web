from django.contrib import admin
from GestionPedidos.models import *

# Register your models here.

class clientes_admin(admin.ModelAdmin):#ESTA CLASE ES SOLO PARA CLIENTES
    list_display=("nombre","telefone")#ESTo NOS AYUDA A MOSTRAR los datos de las tablas EN LA TABLA ADMINISTRACION
    search_fields=("nombre","telefone") #ESTo NOS AYUDA A BUSCAR  DATOS EN LA TABLA ADMINISTRACION
    
class articulos_admin(admin.ModelAdmin):#ESTA CLASE ES SOLO PARA ARTICULOS
    list_filter=("seccion",)# MUESTRA UNA TABLA CON TODOS LOS DATOS FILTRADOS EN ESTE CASO DEPENDIENDO DE LA SECCION
     
class pedidos_admin(admin.ModelAdmin):
    list_display=("numero","entregado")
    list_filter=("fecha",)
    date_hierarchy=("fecha")# muestar un menu con los filtros aplicados

 

    
    
admin.site.register(clientes, clientes_admin)# esto es para agregar la tabla al panel de administracion
admin.site.register(articulos, articulos_admin)#se agrega todo lo necesario que hayamos agregado (todas las tabals que queremos modificar)
admin.site.register(pedidos, pedidos_admin)
