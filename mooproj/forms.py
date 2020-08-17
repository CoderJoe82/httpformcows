from django.forms import modelform_factory
from mooproj.models import Cow

TextForm = modelform_factory(Cow, exclude=[])