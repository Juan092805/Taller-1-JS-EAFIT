from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from search.models import Search
from .models import Wishlist, WishlistItem

class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "wishlist/list.html"
    context_object_name = "items"

    def get_queryset(self):
        wl, _ = Wishlist.objects.get_or_create(user=self.request.user)
        return wl.items.select_related("product").order_by("-created_at")

class ToggleWishlistItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Search, pk=kwargs["pk"])
        wl, _ = Wishlist.objects.get_or_create(user=request.user)
        item, created = WishlistItem.objects.get_or_create(wishlist=wl, product=product)
        if not created:
            item.delete()
            return JsonResponse({"favorited": False})
        return JsonResponse({"favorited": True})
