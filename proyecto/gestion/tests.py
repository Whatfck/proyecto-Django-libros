from django.test import TestCase, Client
from django.urls import reverse
from .models import Autor, Libro
from datetime import date


class AutorViewsTestCase(TestCase):
    """Tests para las vistas de Autor (CRUD)"""
    
    def setUp(self):
        """Crear datos iniciales para las pruebas"""
        self.client = Client()
        self.autor = Autor.objects.create(
            nombre='Juan Pérez',
            correo='juan@ejemplo.com',
            nacionalidad='Colombia',
            fecha_nacimiento=date(1980, 1, 15),
            biografia='Escritor colombiano'
        )
    
    def test_lista_autores_get(self):
        """Test que la vista lista_autores es accesible y retorna 200"""
        response = self.client.get(reverse('gestion:lista_autores'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/lista_autores.html')
        self.assertIn('autores', response.context)
    
    def test_lista_autores_contiene_autor(self):
        """Test que lista_autores muestra los autores creados"""
        response = self.client.get(reverse('gestion:lista_autores'))
        self.assertContains(response, 'Juan Pérez')
    
    def test_crear_autor_get(self):
        """Test que la vista crear_autor es accesible"""
        response = self.client.get(reverse('gestion:crear_autor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/autor_form.html')
    
    def test_crear_autor_post(self):
        """Test que se puede crear un autor vía POST"""
        data = {
            'nombre': 'María García',
            'correo': 'maria@ejemplo.com',
            'nacionalidad': 'España',
            'fecha_nacimiento': '1975-03-20',
            'biografia': 'Escritora española'
        }
        response = self.client.post(reverse('gestion:crear_autor'), data)
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        self.assertTrue(Autor.objects.filter(nombre='María García').exists())
    
    def test_editar_autor_get(self):
        """Test que la vista editar_autor muestra el formulario"""
        response = self.client.get(reverse('gestion:editar_autor', args=[self.autor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/autor_form.html')
    
    def test_editar_autor_post(self):
        """Test que se puede editar un autor"""
        data = {
            'nombre': 'Juan Carlos Pérez',
            'correo': 'juan@ejemplo.com',
            'nacionalidad': 'Colombia',
            'fecha_nacimiento': '1980-01-15',
            'biografia': 'Escritor colombiano actualizado'
        }
        response = self.client.post(
            reverse('gestion:editar_autor', args=[self.autor.pk]), 
            data
        )
        self.assertEqual(response.status_code, 302)
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.nombre, 'Juan Carlos Pérez')
    
    def test_eliminar_autor_get(self):
        """Test que la vista eliminar_autor muestra confirmación"""
        response = self.client.get(reverse('gestion:eliminar_autor', args=[self.autor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/autor_confirm_delete.html')
    
    def test_eliminar_autor_post(self):
        """Test que se puede eliminar un autor"""
        autor_id = self.autor.pk
        response = self.client.post(reverse('gestion:eliminar_autor', args=[autor_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Autor.objects.filter(pk=autor_id).exists())


class LibroViewsTestCase(TestCase):
    """Tests para las vistas de Libro (CRUD)"""
    
    def setUp(self):
        """Crear datos iniciales para las pruebas"""
        self.client = Client()
        self.autor = Autor.objects.create(
            nombre='Carlos López',
            correo='carlos@ejemplo.com',
            nacionalidad='México',
            fecha_nacimiento=date(1985, 6, 10)
        )
        self.libro = Libro.objects.create(
            titulo='Django para Principiantes',
            fecha_publicacion=date(2020, 5, 15),
            genero='Técnico',
            isbn='978-1-234567-89-0',
            autor=self.autor
        )
    
    def test_lista_libros_get(self):
        """Test que la vista lista_libros es accesible"""
        response = self.client.get(reverse('gestion:lista_libros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/lista_libros.html')
        self.assertIn('libros', response.context)
    
    def test_lista_libros_contiene_libro(self):
        """Test que lista_libros muestra los libros creados"""
        response = self.client.get(reverse('gestion:lista_libros'))
        self.assertContains(response, 'Django para Principiantes')
    
    def test_crear_libro_get(self):
        """Test que la vista crear_libro es accesible"""
        response = self.client.get(reverse('gestion:crear_libro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/libro_form.html')
    
    def test_crear_libro_post(self):
        """Test que se puede crear un libro vía POST"""
        data = {
            'titulo': 'Python Avanzado',
            'fecha_publicacion': '2021-07-20',
            'genero': 'Técnico',
            'isbn': '978-0-987654-32-1',
            'autor': self.autor.pk
        }
        response = self.client.post(reverse('gestion:crear_libro'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Libro.objects.filter(titulo='Python Avanzado').exists())
    
    def test_editar_libro_get(self):
        """Test que la vista editar_libro muestra el formulario"""
        response = self.client.get(reverse('gestion:editar_libro', args=[self.libro.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/libro_form.html')
    
    def test_editar_libro_post(self):
        """Test que se puede editar un libro"""
        data = {
            'titulo': 'Django Intermedio',
            'fecha_publicacion': '2020-05-15',
            'genero': 'Educativo',
            'isbn': '978-1-234567-89-0',
            'autor': self.autor.pk
        }
        response = self.client.post(
            reverse('gestion:editar_libro', args=[self.libro.pk]), 
            data
        )
        self.assertEqual(response.status_code, 302)
        self.libro.refresh_from_db()
        self.assertEqual(self.libro.titulo, 'Django Intermedio')
    
    def test_eliminar_libro_get(self):
        """Test que la vista eliminar_libro muestra confirmación"""
        response = self.client.get(reverse('gestion:eliminar_libro', args=[self.libro.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion/libro_confirm_delete.html')
    
    def test_eliminar_libro_post(self):
        """Test que se puede eliminar un libro"""
        libro_id = self.libro.pk
        response = self.client.post(reverse('gestion:eliminar_libro', args=[libro_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Libro.objects.filter(pk=libro_id).exists())
