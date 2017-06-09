from django.shortcuts import render
from django.utils import timezone
from .models import Cards

# Create your views here.
def card_list(request):
    cards = Cards.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'cards/card_list.html', {'cards' : cards})
