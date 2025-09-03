from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406439066',
        'name': 'Prama Ardend Narendradhipa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
