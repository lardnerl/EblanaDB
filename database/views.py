from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
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

