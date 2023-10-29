from django.forms import ModelForm
from updates.models import Updates

class UpdatesForm(ModelForm):
    class Meta:
        model = Updates
        fields = ["title", "content"]