from django.db import models
from django.db.models import Q

class SearchQuerySet(models.QuerySet):
    def by_query(self, q: str):
        return self.filter(name__icontains=q) if q else self

    def by_category(self, cat: str):
        if not cat:
            return self
        # Soporta tanto el campo antiguo (texto) como el nuevo FK
        return self.filter(Q(category__icontains=cat) | Q(category_fk__name__icontains=cat))

class SearchManager(models.Manager.from_queryset(SearchQuerySet)):
    pass
