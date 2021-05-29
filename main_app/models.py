from django.db import models

FEELINGS = (
  ('H', 'Happy'),
  ('Sa', 'Sad'),
  ('Su', 'Surprised'),
  ('A', 'Angry'),
  ('C', 'Confused')
)

# Create your models here.
class Moment(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  month = models.TextField(max_length=100)
  year = models.IntegerField()


def __str__(self):
  return f'{self.name} | {self.year}'


class Many(models.Model):
  date = models.DateField('date')
  people = models.CharField('name', max_length=250)
  feeling = models.CharField(
    max_length= 2,
    choices= FEELINGS,
    default= FEELINGS[0][0]
  )


  moment = models.ForeignKey(Moment, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_feeling_display()} on {self.date}'



  