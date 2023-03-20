from django.db import models
import random,string

# Create your models here.
class url(models.Model):
    url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=20, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_random_string(5)
        super().save(*args, **kwargs)

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        number = string.digits
        return ''.join(random.choice(letters+number) for i in range(length))

    def __str__(self):
        return self.url
