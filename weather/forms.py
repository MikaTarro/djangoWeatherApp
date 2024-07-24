from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'name': 'city',
                                            'id': 'city',
                                            'placeholder': 'Input city name',
                                            'numer': 'filt',
                                            'qwert': 'dewq'
                                            })}

    # <tr><th><label for="city">Name:</label></th><td><input type="text"
    # name="name" value="Mariupol" class="form-control"
    # name="city" id="city" placeholder="Input city name"
    # numer="filt" qwert="dewq" maxlength="30"
    # required></td></tr>

# <tr><th>
# <label for="city">
# Name:</label>
# </th><td>
# <input type="text"
# name="name"
# value="berdyansk"
# class="form-control"
# name="city"
# id="city"
# placeholder="Input city name"
# maxlength="30" required></td></tr>
