from django.apps import AppConfig

class WishlistConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wishlist"

    def ready(self):
        from . import signals  # noqa
