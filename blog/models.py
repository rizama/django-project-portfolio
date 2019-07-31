from django.db import models

class Blog(models.Model):
    title    = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body     = models.TextField()
    image    = models.ImageField(upload_to = 'images/')

    # Merubah Judul Objek pada Admin Page 
    def __str__(self):
        return self.title

    # Membuat Preview Content Post dilimit
    def summary(self):
        return self.body[:100]

    # Membuat Format Waktu pada Blog
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')