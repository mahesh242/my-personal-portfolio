from dal import autocomplete
from master.models import StateMaster, CityMaster
"""To fetch the State name based on auto complete  --starts here"""
class StateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = StateMaster.objects.all()
        if self.q:
            qs = qs.filter(state_name__icontains=self.q)
        return qs

"""To fetch the State name based on auto complete --ends here"""

"""To fetch the City name based on auto complete  --starts here"""
class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CityMaster.objects.all()
        if self.q:
            qs = qs.filter(city_name__icontains=self.q)
        return qs

"""To fetch the City name based on auto complete --ends here"""

