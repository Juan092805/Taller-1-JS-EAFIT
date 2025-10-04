from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Search
from .forms import ProductForm

class ProductListView(ListView):
    model = Search
    template_name = "search/product_list.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        q = self.request.GET.get("q", "").strip()
        cat = self.request.GET.get("category", "").strip()
        return (Search.objects.all()
                .by_query(q)
                .by_category(cat)
                .order_by("name"))

class ProductDetailView(DetailView):
    model = Search
    template_name = "search/product_detail.html"
    context_object_name = "product"

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Search
    form_class = ProductForm
    template_name = "search/product_form.html"
    success_url = reverse_lazy("search:list")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Search
    form_class = ProductForm
    template_name = "search/product_form.html"
    success_url = reverse_lazy("search:list")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Search
    template_name = "search/product_confirm_delete.html"
    success_url = reverse_lazy("search:list")
