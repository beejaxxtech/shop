from .forms import ProductSearchForm



def product_search(request):
    search_form = ProductSearchForm
    if request.method == 'POST':
        search_form = ProductSearchForm(request.POST)
        
        if search_form.is_valid():
            search_form.save()

    return{'search_form' : search_form}     