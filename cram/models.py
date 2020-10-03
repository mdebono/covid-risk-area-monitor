from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    enabled = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Page(models.Model):
    country = models.CharField(max_length=2)
    url = models.URLField()
    xpath_country = models.CharField(max_length=1000, blank=True)
    regex_country = models.CharField(max_length=1000, blank=True)
    xpath_time = models.CharField(max_length=1000, blank=True)
    regex_time = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return '{}: {}'.format(self.country, self.url)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    country = models.CharField('country to monitor', max_length=200)
    enabled = models.BooleanField(default=False)
    def __str__(self):
        return 'user={} page={} country={}'.format(self.user.pk, self.page.pk, self.country)

class Cache(models.Model):
    timestamp = models.DateTimeField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    html = models.TextField()
    def __str__(self):
        return 'page={} timestamp={}'.format(self.page, self.timestamp)
