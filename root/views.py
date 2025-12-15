from categorie.models import Categorie, SousCategorie
from recrutement.models import OffreRecrutement, Postule
from django.shortcuts import render, get_object_or_404, redirect

from recrutement.forms import PostuleForm


def root_index(request):
    # Récupère toutes les catégories avec leurs sous-catégories pour éviter des requêtes supplémentaires
    categories = Categorie.objects.prefetch_related('souscategorie_set').all()

    # Récupère toutes les offres pour les afficher sur la page d'accueil
    offres = OffreRecrutement.objects.select_related('categorie').all()

    context = {
        "categories": categories,
        "offres": offres,
    }

    return render(request, 'index.html', context)


def souscategorie_offres(request, uuid):
    sous = get_object_or_404(SousCategorie, uuid=uuid)
    offres = OffreRecrutement.objects.filter(categorie=sous)

    context = {
        'sous': sous,
        'offres': offres,
    }

    return render(request, 'offres_list.html', context)


def offre_detail(request, uuid):
    offre = get_object_or_404(OffreRecrutement, uuid=uuid)

    if request.method == 'POST':
        form = PostuleForm(request.POST, request.FILES)
        if form.is_valid():
            postule = form.save(commit=False)
            postule.offre = offre
            postule.save()
            return redirect('root_index')
    else:
        form = PostuleForm()

    context = {
        'offre': offre,
        'form': form,
    }

    return render(request, 'offre_detail.html', context)