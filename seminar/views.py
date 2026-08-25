from django.shortcuts import render

def index(request):
    return render(request, 'seminar/index.html')


def topics(request):
    return render(request, 'seminar/topics.html')


def korea(request):
    return render(request, 'seminar/korea.html')


def seminar_detail(request):
    return render(request, 'seminar/korea.html')


def contact(request):
    return render(request, 'seminar/contact.html')