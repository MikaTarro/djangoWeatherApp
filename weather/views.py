import requests
from django.shortcuts import render

from .forms import CityForm
from .models import *


def index(request):
    # print('\n', "----------" , request.method ,'\n')
    appid = "6057c665d1c18eb450a6748428f20338"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        print("-------", form)

        #          <tr><th><label for="city">Name:</label></th><td>
        #  form =  <input type="text" name="name" value="Mariupol" class="form-control"
        #          name="city" id="city" placeholder="Input city name" maxlength="30"
        #          required></td></tr>

        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        print(city)
        res = requests.get(url.format(city.name)).json()
        try:
            city_info = {'city': city.name,
                         'temp': round(res['main']['temp']),
                         'icon': res['weather'][0]['icon']}
        except KeyError:
            pass
        if city_info not in all_cities:
            all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
