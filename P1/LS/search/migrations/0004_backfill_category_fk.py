from django.db import migrations

def backfill(apps, schema_editor):
    Search = apps.get_model('search', 'Search')
    Category = apps.get_model('search', 'Category')
    for prod in Search.objects.all():
        cat_name = (prod.category or '').strip()
        if cat_name:
            cat, _ = Category.objects.get_or_create(name=cat_name)
            prod.category_fk = cat
            prod.save(update_fields=['category_fk'])

class Migration(migrations.Migration):
    dependencies = [
        ('search', '0003_category_fk_productimage'),
    ]

    operations = [
        migrations.RunPython(backfill, migrations.RunPython.noop)
    ]
