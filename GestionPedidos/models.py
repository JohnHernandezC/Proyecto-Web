from django.db import models

#PARA CREAR LAS BASES DE DATOS Y LAS MIGRACIONES 
#PARA HACER LA MIGRACION A POSTGRES SE PSALTA DEL PUNTO 1 AL 3 DESPUES DE HACER LAS RESPECTIVAS CONFIGURACIONES 
"""esto se tiene que registrar en las apps de settings(SOLO ES EL NOMBRE DE LA APP)

para crear la bbdd desde la app se usa
1: python manage.py makemigrations  en el terminal
despues se tiene que hacer la creacion de tablas con el comando
2: python manage.py sqlmigrate GestionPedidos Y EL NUMERO DE LA MIGRACION QUE APARECE EN CONSOLA EN ESTE CASO 0001
ahora se utiliza el comando 
3: python manage.py migrate ESTO PARA USAR EL LENGUJE SQL Y CREAR LAS TABLAS
# PARA trabajar con posgres se debe intalar la libreria  pip install psycopg2
#Y luego se configura en settings database

# se crean las tabalas de las bases de datos para msql"""
class clientes (models.Model):
    nombre=models.CharField(max_length=30, verbose_name="El Nombre")#verbose_name="El Nombre"
    # esto es para cuando queremos que en la barrra de administracion aparesca el campo con un nombre espesifico(no necesita migracion)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    #email=models.EmailField(blank=True, null=True)  Esto es si queremos que un campo sea opcional
    #NO OLVIDAR QUE DESPUES DE CADA MODIFICACION SE DEBE HACER UNA MIGRACION
    #python manage.py makemigrations  
    #python manage.py migrate SE USAN LOS DOS
    telefone=models.CharField(max_length=12)
    def __str__(self):
        return self.nombre #esto nos muestra el o los datos espesificos de la tabla administracion
    #se muestran en una sola casilla ¡¡usar solo 1!!
    
class articulos (models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    percio=models.IntegerField()
    def __str__(self):
        return self.nombre
    
class pedidos (models.Model):
    numero=models.IntegerField()
    fecha=models.DateTimeField()
    entregado=models.BooleanField()
    
    def __str__(self): 
        return self.numero
  
#Estos modelos se registran en la clase admin


    

    