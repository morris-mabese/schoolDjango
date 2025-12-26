from django.shortcuts import render

def home(request):
    return render(request, 'home.html',  {})

def about(request):
    return render(request, 'about.html',  {})

def classes(request):
    return render(request, 'classes.html',  {})

def teachers(request):
    return render(request, 'teachers.html',  {})

def career(request):
    return render(request, 'career.html',  {})

def facility(request):
    return render(request, 'facility.html',  {})

def testimonial(request):
    return render(request, 'testimonial.html',  {})

def contact(request):
    return render(request, 'contact.html',  {})

def departmental_heads(request):
    return render(request, 'departmental-heads.html',  {})

def vacancy(request):
    return render(request, 'vacancy.html', {})

def requirement(request):
    return render(request, 'requirement.html', {})

def history(request):
    return render(request, 'history.html', {})

def managing_director_message(request):
    return render(request, 'managing-director-message.html', {})

def bod_message(request):
    return render(request, 'bod-message.html', {})


def fees_structure(request):
    return render(request, 'fees-structure.html', {})