# Proyecto Django_libros - Taller 2 Django

Este proyecto consiste en el diseño de una aplicación en Django con dos modelos con enfoque de base de datos relacional para el almacenamiento y gestión de libros y autores.

---

## 👥 Asignación de Tareas (Equipo de 3)

### 🛠️ Dev 1: Infraestructura y Modelos (Arquitecto de Datos)
*   **Paso 1:** Configuración del entorno de desarrollo (Venv, pip).
*   **Paso 2:** Creación del proyecto Django.
*   **Paso 3:** Creación de la aplicación `gestion`.
*   **Paso 4:** Registro de la aplicación en `settings.py`.
*   **Paso 5:** Diseño de modelos (`Autor` y `Libro`) en `models.py`. Ejecución de migraciones y creación del Superuser.
*   **Paso 6:** Registro de modelos en `admin.py` con filtros y visualización personalizada.

### ⚙️ Dev 2: Lógica de Negocio y Rutas (Desarrollador Backend)
*   **Paso 7:** Creación de formularios (`forms.py`) para `Autor` y `Libro`.
*   **Paso 8:** Implementación de las Vistas CRUD (Listar, Crear, Editar, Eliminar) para ambos modelos.
*   **Paso 8.1:** Configuración de las URLs de la aplicación (`gestion/urls.py`) y enlace con las URLs principales del proyecto.

### 🎨 Dev 3: Interfaz de Usuario y Despliegue (Desarrollador Frontend/DevOps)
*   **Paso 9:** Implementación de Templates HTML utilizando Herencia de Plantillas (`base.html`).
*   **Paso 10:** Mejora visual integrando **Bootstrap** para un diseño moderno y responsive.
*   **Paso 11:** Investigación y configuración para el despliegue (Railway, Render o PythonAnywhere).
*   **Finalización:** Generación de `requirements.txt` y `Procfile`.

---

## 📖 Guía de Implementación del Proyecto

### Paso 1. Configuración del entorno
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install django
```

### Paso 2. Crear el proyecto
```bash
django-admin startproject proyecto
```

### Paso 3. Crear aplicación "gestion"
```bash
cd proyecto
python manage.py startapp gestion
```

### Paso 5. Modelos (models.py)
#### Modelo Autor
```python
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):  
        return self.nombre  
```

#### Modelo Libro
```python
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")  

    def __str__(self):  
        return self.titulo  
```

### Paso 6. Admin (admin.py)
```python
@admin.register(Autor)
class AutorAdmin(models.ModelAdmin):
    list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')

@admin.register(Libro)
class LibroAdmin(models.ModelAdmin):
    list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
    list_filter = ('autor', 'genero', 'fecha_publicacion')
```

### Paso 9. Estructura de Templates
Los archivos deben ubicarse en `templates/gestion/`:
- `base.html` (Layout principal)
- `lista_autores.html` / `lista_libros.html`
- `autor_form.html` / `libro_form.html`
- `autor_confirm_delete.html` / `libro_confirm_delete.html`

---

> [!IMPORTANT]
> **Mejora Visual:** Se requiere el uso de Bootstrap para que la aplicación tenga una estética profesional y premium.