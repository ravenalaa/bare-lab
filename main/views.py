from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Claudia Paskalia Koesno',
        'npm': '2306275355',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)