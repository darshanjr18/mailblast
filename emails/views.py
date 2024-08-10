from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserDetailForm
from django.core.mail import send_mail
from .models import UserDetail
from .forms import UserDetailForm


def home(request):
    return render(request, 'home.html')

def submit_details(request):
    if request.method == "POST":
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after successful submission
    else:
        form = UserDetailForm()

    return render(request, 'submit_details.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def send_bulk_emails(request):
    users = UserDetail.objects.all()
    email_list = [user.email for user in users]

    send_mail(
        'Subject of the Email',
        'This is the body of the email.',
        'potatoboi1817@gmail.com',  # From email
        email_list,
        fail_silently=False,
    )

    return render(request, 'email_sent.html')


