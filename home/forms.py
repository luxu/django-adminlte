import os

from django import forms
from django.forms.models import inlineformset_factory

from . import models

class MyDateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        super().__init__(format="%Y-%m-%d")


class BaseMeta:
    exclude = ("deleted", "status")

class PecasForm(forms.ModelForm):
    class Meta(BaseMeta):
        model = models.Pecas


class ItensPecasForm(forms.ModelForm):
    class Meta(BaseMeta):
        model = models.Itenspecas
#
#
# class ComercioForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_tag = False
#
#         self.helper.layout = Layout(
#             Div(Field("description"), wrapper_class="col-md-12"),
#             Div(
#                 FormActions(
#                     Submit("submit", _("Submit"), css_class="btn btn-primary"),
#                     css_class="col-sd-12",
#                 )
#             ),
#         )
#
#     class Meta(BaseMeta):
#         model = models.Comercio


# ItemPecasFormSet = inlineformset_factory(
#     models.Pecas,
#     models.Itenspecas,
#     form=ItensPecasForm,
#     fields=["description", "pecas", "price", "quantity", "subtotal"],
#     extra=1,
#     can_delete=True,
# )


# class EventsForm(forms.ModelForm):
#     class Meta:
#         model = models.Events
#         fields = [
#             "description", "event_date"
#         ]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_tag = False
#         self.fields["event_date"].localize = True
#         self.fields["event_date"].widget = MyDateInput()
#
#         self.helper.layout = Layout(
#             Div(
#                 # Field("description", wrapper_class="col-md-12"),
#                 # Field("event_date", wrapper_class="col-md-12"),
#             ),
#             Div(
#                 FormActions(
#                     Submit("submit", _("Submit"), css_class="btn btn-primary"),
#                     css_class="col-md-12",
#                 )
#             ),
#         )
#
#
class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = ["description"]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_tag = False
#
#         self.helper.layout = Layout(
#             Div(
#                 Field("description", wrapper_class="col-md-12"),
#             ),
#             Div(
#                 FormActions(
#                     Submit("submit", _("Submit"), css_class="btn btn-primary"),
#                     css_class="col-md-12",
#                 )
#             ),
#         )
