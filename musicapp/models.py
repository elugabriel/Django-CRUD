from django.db import models

# Create your models here.
class Lyric(models.Model):
    content = models.CharField(max_length = 200)
    song_id = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length = 200)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id= models.IntegerField()
    lyric = models.ForeignKey(Lyric, on_delete = models.CASCADE)

    def __str__(self):
        return self.title, self.date_released, self.likes, self.artiste_id


class Artiste(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()
    song = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name, self.age






