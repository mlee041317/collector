from django.db import models

FEELINGS = (
  ('Happy'),
  ('Sad'),
  ('Surprised'),
  ('Angry'),
  ('Confused')
)

# Create your models here.
class Moment(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  month = models.TextField(max_length=100)
  year = models.IntegerField()


def __str__(self):
  return f'{self.name} | {self.year}'


class New(models.Model):
  date = models.DateField()
  people = models.CharField(max_length=250)
  feeling = models.CharField(
    max_length=1,
    choices= FEELINGS,
    default= FEELINGS[0][0]
  )



moment = models.ForeignKey(Moment, on_delete=models.CASCADE)

def __str__(self):
  return f'{self.get_feeling_display()} on {self.date}'



  