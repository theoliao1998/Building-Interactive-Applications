from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from stars.models import Star, Type
from stars.forms import TypeForm

# Create your views here.

class StarList(LoginRequiredMixin, View) :
    def get(self, request):
        bc = Type.objects.all().count();
        cl = Star.objects.all();

        ctx = { 'type_count': bc, 'star_list': cl };
        return render(request, 'stars/star_list.html', ctx)

class TypeView(LoginRequiredMixin,View) :
    def get(self, request):
        bl = Type.objects.all();
        ctx = { 'type_list': bl };
        return render(request, 'stars/type_list.html', ctx)

# We use reverse_lazy() because we are in "constructor code"
# that is run before urls.py is cmopletely loaded
class TypeCreate(LoginRequiredMixin, View):
    template = 'stars/type_form.html'
    success_url = reverse_lazy('stars:all')
    def get(self, request) :
        form = TypeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = TypeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        type = form.save()
        return redirect(self.success_url)

class TypeUpdate(LoginRequiredMixin, View):
    model = Type
    success_url = reverse_lazy('stars:all')
    template = 'stars/type_form.html'
    def get(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=type)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(request.POST, instance = type)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('stars:all')
    template = 'stars/type_confirm_delete.html'

    def get(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=type)
        ctx = { 'type': type }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        type.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class StarCreate(LoginRequiredMixin,CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

# We use reverse_lazy rather than reverse in the constructor attributes below
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/#createview