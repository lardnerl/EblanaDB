from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, View, ListView, UpdateView
from database.models import Character

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)
   
        
def index(request):
    return HttpResponse("Hello, world. You're at the database index.")
    
class ListCharacterView(ListView):

    model = Character
    template_name = 'character_list.html'
    
    
class CreateCharacterView(CreateView):

    model = Character
    template_name = 'edit_character.html'
    
    def get_success_url(self):
        return reverse('character-list')
        
    def get_context_data(self, **kwargs):

        context = super(CreateCharacterView, self).get_context_data(**kwargs)
        context['action'] = reverse('character-new')

        return context
        
class UpdateCharacterView(UpdateView):

    model = Character
    template_name = 'edit_character.html'

    def get_success_url(self):
        return reverse('character-list')
        
    def get_context_data(self, **kwargs):

        context = super(UpdateCharacterView, self).get_context_data(**kwargs)
        context['action'] = reverse('character-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class CharacterView(DetailView):

    model = Character  

    template_name = 'character.html'