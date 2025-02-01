from django.shortcuts import render


def homepage(request):
    name = "Alexandre"
    person = {"name": "Alexandre Rogério", "age": 31, "city": "Uberlândia"}
    return render(request, "home.html", {"name": name, "person": person})


def about(request):
    certifications = ["React", "Django", "Docker", "Python", "Spring"]
    return render(request, "about.html", {"certifications": certifications})
