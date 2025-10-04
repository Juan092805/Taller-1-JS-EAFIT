#  Taller 01 – JS-EAFIT

Juan Manuel Castellanos

Juan Pablo Betancourt

Nota importante: Profe no pudimos subir el proyecto original de Proyecto Integrador 1 entonces nos toco editarlo y subirlo directamente sin que se vean las branch.

Proyecto base desarrollado en **Django** para el curso de Ingeniería de Software.  
Este repositorio contiene las soluciones del Taller 01.

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
---
---

### ✅ Actividad 5 – Patrones de Diseño en Django

En esta actividad se aplicaron patrones propios de Django tanto en **Modelos** como en **Vistas**:

- **Normalización en Modelos**:  
  Se creó una nueva app llamada `wishlist` con los modelos `Wishlist` y `WishlistItem`, separados de `Search`.  
  Esto permitió aplicar una estructura **normalizada** para la relación `Usuario ↔ Productos en lista de deseos`.  
  Además, se usó `unique_together` en `WishlistItem` para evitar duplicados y mantener la integridad de los datos:contentReference[oaicite:6]{index=6}.

- **Vistas basadas en clases (CBV)**:  
  Se implementó `MyWishlistView` (basada en `ListView`) para mostrar los productos de la lista de deseos de un usuario autenticado, y `ToggleWishlistItemView` para agregar o quitar productos mediante AJAX, siguiendo el patrón CRUD con CBVs:contentReference[oaicite:7]{index=7}.

- **Señales (Signals)**:  
  Se implementó un `pre_save` en `Search` para detectar cambios de precio.  
  Si el precio bajaba, se notificaba automáticamente a los usuarios que tenían ese producto en su wishlist, aplicando el patrón **Observer** mediante signals:contentReference[oaicite:8]{index=8}.

 Con esto se cumplieron **dos patrones de diseño diferentes en Django**:  
- **Normalización de modelos**.  
- **Vistas basadas en clases (CBV)** con separación clara de responsabilidades.  

---

###  BONUS – Nueva funcionalidad con patrón aplicado

Como funcionalidad extra, se implementó un **Wishlist con notificaciones de bajada de precio**:  

- Los usuarios pueden marcar productos con una estrella para agregarlos o quitarlos de su lista de deseos:contentReference[oaicite:9]{index=9}.  
- Si el precio de un producto baja (detectado con signals), se lanza una notificación al usuario usando el servicio de notificaciones basado en **Singleton** de la Actividad 4:contentReference[oaicite:10]{index=10}.  
- Se añadieron templates dedicados (`wishlist/templates/wishlist/list.html`) y herencia de `base.html` para mantener consistencia visual:contentReference[oaicite:11]{index=11}.  

Decisión de diseño:  
- Se eligió **Observer (Signals)** para escuchar cambios en productos sin acoplar la lógica directamente al modelo.  
- Se reutilizó el **Singleton NotificacionService** como servicio centralizado, aplicando inversión de dependencias y asegurando que toda la app use un único punto de notificación.  

---
