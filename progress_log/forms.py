from django import  forms
from .models import Topic, AboutTopic

class TopicForm(forms.ModelForm):
    # Allowing users to create personal topics
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}    # Empty label

class AboutTopicForm(forms.ModelForm):
    # Allowing users to create personal home pages for topics (home page is made of multiple AboutTopic blocks)
    class Meta:
        model = AboutTopic
        fields = ['title','image','text']
        labels = {'title':'', 'image':'','text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
