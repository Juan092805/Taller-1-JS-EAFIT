#  Taller 01 – JS-EAFIT

Juan Manuel Castellanos
Juan Pablo Betancourt
Proyecto base desarrollado en **Django** para el curso de Ingeniería de Software.  
Este repositorio contiene las soluciones de las **Actividades 1 a 4** del Taller 01.

---

##  Contenido del Taller

###  Actividad 1 – Repositorio
El proyecto fue migrado a este repositorio  para no alterar la versión original.  
Se incluye un archivo [`setup.txt`](./setup.txt) con instrucciones de instalación y ejecución.

---

###  Actividad 2 – Revisión Autocrítica

#### Usabilidad
- ✔ Interfaces simples y navegación clara.  
- ✘ Falta validación de formularios más amigable.  
- **Mejora propuesta:** agregar validación frontend y mensajes de error descriptivos.  

#### Compatibilidad
- ✔ Funciona en navegadores modernos.  
- ✘ No se han probado versiones móviles.  
- **Mejora propuesta:** aplicar responsive design (Bootstrap o TailwindCSS).  

#### Rendimiento
- ✔ Consultas a la base de datos sencillas y eficientes.  
- ✘ Las imágenes no están optimizadas.  
- **Mejora propuesta:** configurar `ImageField` con Pillow y optimización de recursos estáticos.  

#### Seguridad
- ✔ Uso del sistema de autenticación de Django.  
- ✘ Formularios sin protección CSRF en algunos casos.  
- **Mejora propuesta:** incluir `{% csrf_token %}` en todos los formularios POST y habilitar HTTPS.  

---

###  Actividad 3 – Inversión de Dependencias

Antes, las vistas accedían directamente a los modelos:  

```python
# views.py (antes)
productos = Producto.objects.all()

Ahora, se aplica **Repository Pattern** para desacoplar la vista del modelo:  

# repositories/producto_repository.py
from ..models import Producto

class ProductoRepository:
    def get_all(self):
        return Producto.objects.all()
# views.py
from .repositories.producto_repository import ProductoRepository

def lista_productos(request):
    repo = ProductoRepository()
    productos = repo.get_all()
    return render(request, "productos.html", {"productos": productos})
```

---

###  Actividad 4 – Patrón de Diseño en Python

Se aplicó el **Patrón Singleton** en un servicio de notificaciones centralizado.  
Este patrón asegura que solo exista **una instancia** de la clase en toda la aplicación, lo cual es útil para servicios globales como notificaciones, logs o conexiones a APIs externas.

####  Implementación

```python
# services/notificacion_service.py
class NotificacionService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificacionService, cls).__new__(cls)
        return cls._instance

    def enviar(self, mensaje, usuario):
        print(f"Notificación para {usuario}: {mensaje}")
```

####  Uso en vistas

```python
from .services.notificacion_service import NotificacionService
from django.shortcuts import render

def confirmar_compra(request):
    servicio = NotificacionService()
    servicio.enviar("Tu compra fue confirmada", request.user.username)
    return render(request, "confirmacion.html")
```
