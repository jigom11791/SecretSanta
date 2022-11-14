from django.db import models

# Create your models here.
class Participants(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    selected = models.BooleanField(default=False)
    suggestions = models.TextField()

    def __str__(self):
        return self.name
    
    def is_selected(self):
        return self.selected
    
    def select(self):
        if not self.select:
            self.select = True
            return True
        else:
            return False

class Pairs(models.Model):
    give = models.ForeignKey('Participants', on_delete=models.CASCADE)
    receive = models.ForeignKey('Participants', on_delete=models.CASCADE, related_name='recieve')

    def __str__(self):
        return f'{self.give} => {self.receive}'