from django import  forms
from .models import Topic

class TopicForm(forms.ModelForm):
    # Allowing users to create personal topics
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}    # Empty label