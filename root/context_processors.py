from categorie.models import Categorie


def categories(request):
    """Expose les catégories et leurs sous-catégories à tous les templates."""
    qs = Categorie.objects.all().prefetch_related('souscategorie_set')
    return {
        'categories': qs,
    }
