from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('fullname','book_code','position')
        labels = {'fullname':'Book Name',
                  'book_code':'BookCode'
                  }

    def __init__(self, *args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['book_code'].required = False







from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']