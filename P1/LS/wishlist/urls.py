from django.urls import path
from .views import MyWishlistView, ToggleWishlistItemView

app_name = "wishlist"
urlpatterns = [
    path("", MyWishlistView.as_view(), name="mine"),
    path("toggle/<int:pk>/", ToggleWishlistItemView.as_view(), name="toggle"),
]
