from django.shortcuts import render
from .forms import NameForm
from .models import UserName

def home(request):
    greeting = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].strip()
            if name:
                user_name = UserName.objects.create(name=name)
                greeting = f'Привет, {user_name.name}!'
            else:
                form.add_error('name', 'Поле имени не может быть пустым.')
    else:
        form = NameForm()

    return render(request, 'greetapp/home.html', {'form': form, 'greeting': greeting})
