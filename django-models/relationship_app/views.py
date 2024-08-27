from django.shortcuts import render
from .models import Book

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login

# Login View - using Django's built-in view
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

# Logout View - using Django's built-in view
class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'

relationship_app/member_view.html", "relationship_app/librarian_view.html", "relationship_app/admin_view.html"]

# Registration View - using a custom view based on Django's UserCreationForm
class RegisterView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
     

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
    

from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'