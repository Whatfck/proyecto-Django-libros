# proyecto-Django-libros
## Taller 2 Django almacenamiento de libros

En grupos de 3 diseña una aplicación en Django con dos modelos con el enfoque de base de
datos relacional, el proyecto cuenta con dos modelos para una sola aplicación.

**Sigue los siguientes pasos.**

**Paso 1. Configuración del entorno de desarrollo**

```console
python -m venv venv
venv\Scripts\activate # Windows
pip install django
```

**Paso 2. Crear el proyecto**
```console
django-admin startproject proyecto
```

**Paso 3. Crear aplicación gestión dentro del proyecto**
```console
cd proyecto
python manage.py startapp gestion
```

**Paso 4. Registrar la aplicacion en los settings**
```console
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'gestion',
]
```

**Paso 5. Crear modelo, autor y libros en models.py**
```console
python manage.py createsuperuser # crear super usuario
python manage.py makemigrations
python manage.py migrate

Autor
---------------------------
id (PK)
nombre
correo
nacionalidad
fecha_nacimiento
biografia
|
| 1
|
| *
Libro
---------------------------
id (PK)
titulo
fecha_publicacion
genero
isbn
autor_id (FK -> Autor.id)
```

**Modelo autor**
**Modelo Autor (campos) models .py aplicación Gestión**

| Campo | Tipo de Dato | Descripción |
|-------|--------------|-------------|
| id    | AutoField    | Llave primaria |
| nombre | CharField   | Nombre completo del autor |
| correo | EmailField  | Correo electrónico único |
| nacionalidad | CharField | Nacionalidad del autor |
| fecha_nacimiento | DateField | Fecha de nacimiento del autor |
| biografia | TextField   | Breve biografía |

**Codigo Python**
```python
class Autor(models.Model):
nombre = models.CharField(max_length=100)
correo = models.EmailField(unique=True)
nacionalidad = models.CharField(max_length=50)
fecha_nacimiento = models.DateField()
biografia = models.TextField(blank=True, null=True)
def __str__(self):
return self.nombre
Autor
---------------------------
id (PK)
nombre
correo
nacionalidad
fecha_nacimiento
biografia
|
| 1
|
| *
Libro
---------------------------
id (PK)
titulo
fecha_publicacion
genero
isbn
autor_id (FK -> Autor.id)
```
Modelo Libro (campos adicionales)
**Modelo libro**
**Modelo libro (campos) models .py aplicación Gestión**

| Campo | Tipo de Dato | Descripción |
|-------|--------------|-------------|
| id    | AutoField    | Llave primaria |
| titulo | CharField   | Título del libro |
| fecha_publicacion | DateField | Fecha de publicación |
| genero | CharField   | Género literario del libro |
| isbn | CharField   | Código ISBN |
| autor | ForeignKey  | Llave foránea a Autor |

```python
class Libro(models.Model):
titulo = models.CharField(max_length=150)
fecha_publicacion = models.DateField()
genero = models.CharField(max_length=50)
isbn = models.CharField(max_length=20, unique=True)
autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
def __str__(self):
return self.titulo
```

**Paso 6. Registrar el modelo en el administrador**
código admin.py
```python
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
list_filter = ('autor', 'genero', 'fecha_publicacion')
```

**Paso 7. Diseñar el Formulario (forms.py)**
```python
class AutorForm(forms.ModelForm):
class Meta:
model = Autor
fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
class LibroForm(forms.ModelForm):
class Meta:
model = Libro
fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
```

Paso 8. Diseñar las vistas de los forularios realizando un ***CRUD***

*Ejercicio evaluativo, diseñe vistas genéricas para cada método del ***CRUD***, en templates diferentes.*

**views.py**
```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
# CRUD Autores
def lista_autores(request):
autores = Autor.objects.all()
return render(request,'gestion/lista_autores.html',{'autores':autores})
def crear_autor(request):
if request.method=='POST':
form = AutorForm(request.POST)
if form.is_valid():
form.save()
return redirect('lista_autores')
else:
form = AutorForm()
return render(request,'gestion/autor_form.html',{'form':form})
def editar_autor(request, pk):
autor = get_object_or_404(Autor, pk=pk)
if request.method=='POST':
form = AutorForm(request.POST, instance=autor)
if form.is_valid():
form.save()
return redirect('lista_autores')
else:
form = AutorForm(instance=autor)
return render(request,'gestion/autor_form.html',{'form':form})
def eliminar_autor(request, pk):
autor = get_object_or_404(Autor, pk=pk)
if request.method=='POST':
autor.delete()
return redirect('lista_autores')
return render(request,'gestion/autor_confirm_delete.html',{'autor':autor})
```

**Paso 8. Aplicación de urals en la aplicación Gestión/urls.py**

Ejercicio evaluativo, diseñe urls para las vistas genéricas para cada método del ***CRUD***
```python
from django.urls import path
from . import views
urlpatterns = [
path('autores/', views.lista_autores, name='lista_autores'),
path('autores/crear/', views.crear_autor, name='crear_autor'),
path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
path('autores/eliminar/<int:pk>/', views.deleteview, name='eliminar_autor'),
]
```

**Paso 8.1 importe las urls de la aplicación gestión en proyecto/urls.py**
```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('gestion.urls')),
]
```

**Paso 9. Implementación de los templates para cada una de las acciones de la app**

**Templates HTML básicos**

**lista_autores.html**

```html
<h1>Autores</h1>
<a href="{% url 'crear_autor' %}">Agregar Autor</a>
<ul>
{% for autor in autores %}
<li>{{ autor.nombre }} - {{ autor.correo }}
<a href="{% url 'editar_autor' autor.pk %}">Editar</a>
<a href="{% url 'eliminar_autor' autor.pk %}">Eliminar</a>
</li>
{% endfor %}
</ul>
```

**autor_form.html**

```html
<h1>Formulario Autor</h1>
<form method="post">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Guardar</button>
</form>
```

**autor_confirm_delete.html**

```html
<h1>Eliminar Autor</h1>
<p>¿Desea eliminar {{ autor.nombre }}?</p>
<form method="post">
{% csrf_token %}
<button type="submit">Sí, eliminar</button>
</form>
```

**Estructura del proyecto**

```text
admin_libros/ ← Carpeta raíz del proyecto
│
├── manage.py ← Script principal para ejecutar comandos de
Django
│
├── admin_libros/ ← Carpeta de configuración global del
proyecto
│ ├── __init__.py
│ ├── settings.py ← Configuración general (BD, apps, rutas de
templates, etc.)
│ ├── urls.py ← Enrutamiento principal del proyecto
│ ├── asgi.py ← Configuración ASGI (opcional)
│ └── wsgi.py ← Configuración WSGI (para despliegue)
│
├── gestion/ ← Aplicación principal (módulo de
administración de libros)
│ ├── __init__.py
│ ├── admin.py ← Registro de modelos para el panel de
administración
│ ├── apps.py ← Configuración de la app
│ ├── forms.py ← Formularios personalizados (AutorForm,
LibroForm)
│ ├── models.py ← Definición de modelos (Autor, Libro)
│ ├── urls.py ← Rutas específicas de la app
│ ├── views.py ← Lógica de negocio (CRUD)
│ │
│ ├── migrations/ ← Carpeta autogenerada por Django (historial
de base de datos)
│ │ └── __init__.py
│ │
│ ├── templates/ ← Plantillas HTML
│ │ └── gestion/ ← Subcarpeta de templates para la app
│ │ ├── base.html ← Plantilla base (opcional)
│ │ ├── lista_autores.html ← Listado de autores
│ │ ├── autor_form.html ← Formulario crear/editar autor
│ │ ├── autor_confirm_delete.html ← Confirmación de eliminación
│ │ ├── lista_libros.html ← Listado de libros
│ │ ├── libro_form.html ← Formulario crear/editar libro
│ │ └── libro_confirm_delete.html ← Confirmación de eliminación
```

**Mejorar la interfaz (opcional)**
- **Integrar Bootstrap o TailwindCSS para mejorar los formularios y listas.**
- **Ejemplo de inclusión de Bootstrap en base.html:**

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
rel="stylesheet">
```

**Paso 10. Despliegue**
Investigar cómo se puede desplegar el app con las siguientes tecnologías:
- **Railway, Render o PythonAnywhere** para subir la app.
- Configurar archivos requirements.txt y Procfile para desplega