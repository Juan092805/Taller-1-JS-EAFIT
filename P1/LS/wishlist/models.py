from django.db import models
from django.contrib.auth import get_user_model
from search.models import Search

User = get_user_model()

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wishlist")
    def __str__(self): return f"Wishlist de {self.user}"

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Search, on_delete=models.CASCADE, related_name="wishlisted_in")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("wishlist", "product")

    def __str__(self): return f"{self.product} en {self.wishlist}"
