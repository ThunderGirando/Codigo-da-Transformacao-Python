from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q 
from .models import Product

class ProductListView(ListView):
    # Listagem, Busca e Paginação (Read)
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 5 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            # Filtra por nome (case-insensitive)
            queryset = queryset.filter(Q(name__icontains=search_query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ProductCreateView(CreateView):
    # Cadastro (Create)
    model = Product
    fields = ['name', 'description', 'price', 'quantity']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    # Atualização (Update)
    model = Product
    fields = ['name', 'description', 'price', 'quantity']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    # Exclusão (Delete)
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')