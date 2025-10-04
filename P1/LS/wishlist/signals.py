from django.db.models.signals import pre_save
from django.dispatch import receiver
from search.models import Search
from .models import WishlistItem
from .services.notificacion_service import NotificacionService

@receiver(pre_save, sender=Search)
def notify_price_drop(sender, instance: Search, **kwargs):
    if not instance.pk:
        return
    try:
        old = Search.objects.get(pk=instance.pk)
    except Search.DoesNotExist:
        return
    if instance.price < old.price:
        servicio = NotificacionService()
        items = WishlistItem.objects.filter(product=instance).select_related("wishlist__user")
        for it in items:
            servicio.enviar(
                f"¡Bajó de precio! {instance.name} ahora cuesta ${instance.price}",
                it.wishlist.user.username
            )
