from django.db import models

# Create your models here.
class Topic(models.Model):
    # A topic the user is making progress on
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns model as a string
        return self.text

class AboutTopic(models.Model):
    # Home page for associated Topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default=Topic.__name__)    # Section title for each block created for AboutTopic
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'about_topics'

    def __str__(self):
        # Returns as a string that's 50 characters max
        return  f"{self.title[:50]}..."

class Entry(models.Model):
    # Something specific learned/done about topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default=Topic.__name__)    # My own personal addition while doing python book's tutorial :)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Returns entry as a string that's 50 characters max
        return  f"{self.title[:50]}..."     # Python book said to do self.text[:50] but I used self.title[:50]
