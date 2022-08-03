from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    import requests
    import json

    context = {}

    regions = ['Вінницька область', 'Волинська область', 'Дніпропетровська область', 'Донецька область',
               'Житомирська область', 'Закарпатська область', 'Запорізька область', 'Івано-Франківська область',
               'Київська область', 'м. Київ', 'Кіровоградська область', 'Луганська область', 'Львівська область',
               'Миколаївська область', 'Одеська область', 'Полтавська область', 'Рівненська область', 'Сумська область',
               'Тернопільська область', 'Харківська область', 'Херсонська область', 'Хмельницька область',
               'Черкаська область', 'Чернівецька область', 'Чернігівська область']

    r = requests.get('http://map-static.vadimklimenko.com/statuses.json')
    binary = r.content
    jsonout = json.loads(binary)
    i = 1
    for reg in regions:
        context["id" + str(i)] = jsonout["states"][reg]["enabled"]
        i += 1
    return render(request, 'alert/index.html', context)


