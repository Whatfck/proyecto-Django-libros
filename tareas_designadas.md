# Proyecto Django_libros - Taller 2 Django

Este proyecto consiste en el diseño de una aplicación en Django con dos modelos con enfoque de base de datos relacional para el almacenamiento y gestión de libros y autores.

---

## 👥 Asignación de Tareas (Equipo de 2)

### 🛠️ Dev 1: Estructura, Modelos e Interfaz (Arquitecto & Frontend)
*   **Paso 1-4:** Configuración del entorno, creación del proyecto y la app `gestion`.
*   **Paso 5:** Diseño de modelos (`Autor` y `Libro`) y ejecución de migraciones.
*   **Paso 6:** Registro de modelos en el panel `admin.py`.
*   **Paso 9:** Implementación de Templates HTML (`base.html`, listas y formularios).
*   **Paso 10:** Mejora visual integral utilizando **Bootstrap** para un diseño premium.

### ⚙️ Dev 2: Lógica de Negocio, Rutas y Despliegue (Backend & DevOps)
*   **Paso 7:** Creación de formularios (`forms.py`) para los modelos.
*   **Paso 8:** Implementación de todas las Vistas CRUD (Listar, Crear, Editar, Eliminar).
*   **Paso 8.1:** Configuración y enlace de todas las URLs del proyecto.
*   **Paso 11:** Investigación y configuración del despliegue (Railway/Render).
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

IMPORTANTE: Se requiere el uso de Bootstrap para que la aplicación tenga una estética profesional y premium.
