from django.contrib import admin
from django.forms import TextInput

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget(attrs={'class': 'vPhoneNumberField'})},
    }

    list_display = ('name', 'email', 'phone_number')

    # Exclude the 'id' field from the list view
    exclude = ('id',)

    search_fields = ('name', 'email', 'phone_number')


admin.site.register(Person, PersonAdmin)
