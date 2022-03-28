from django.shortcuts import render, get_object_or_404
from store.models import Product
from catagories.models import Category


# Create your views here.
def store(request, category_slug=None):
    category = None
    product = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category, is_available=True)
        product_count = product.count()
    else:
        product = Product.objects.all().filter(is_available=True)
        product_count = product.count()
    context = {
        'product': product,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
