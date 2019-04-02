from django.contrib import admin
from .models import Verbum, Conjugation

# TILFØJ 'AT' FORAN ET DANSK VERBUM:
def add_prefix_at_to_danish(modeladmin, request, queryset):
	for verbum in queryset:
		if verbum.danish[:3] != 'at ':
			verbum.danish = 'at ' + verbum.danish
			if verbum.extra:
				if verbum.extra[:3] != 'at ':
					verbum.extra = 'at ' + verbum.extra

			verbum.save()
      
# TILFØJ PERSONLIGE PRONOMINER TIL REFLEKSIVE VERBER:
def add_pronoun(modeladmin, request, queryset):
	for conjugation in queryset:
		conjugation.p1_s = 'me ' + conjugation.p1_s
		conjugation.p2_s = 'te ' + conjugation.p2_s
		conjugation.p3_s = 'se ' + conjugation.p3_s
		conjugation.p1_p = 'nos ' + conjugation.p1_p
		conjugation.p2_p = 'os ' + conjugation.p2_p
		conjugation.p3_p = 'se ' + conjugation.p3_p

		conjugation.save()
