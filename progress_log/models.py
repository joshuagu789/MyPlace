from django.db import models

# Create your models here.
class Topic(models.Model):
    # A topic the user is making progress on
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns model as a string
        return self.text

class Entry(models.Model):
    # Something specific learned/done about topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default=str(Topic))    # My own personal addition while doing python book's tutorial :)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Returns entry as a string that's 50 characters max
        return  f"{self.title[:50]}..."     # Python book said to do self.text[:50] but I used self.title[:50]
