from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from User.models import Eleve, Enseignant
from ENSISmart.models import TemporaryLink
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def note_main_view(request):
    return render(request, 'main_note.html')
