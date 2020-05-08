from django.db import models
# Create your models here.


class Exp(models.Model):
    exp = models.CharField('expression', max_length=150, db_index=True)
    result_of_exp = models.CharField('result of expression', max_length=150, db_index=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    expressions = models.Manager()

    def __str__(self):
        return '{} {} {}'.format(self.exp, self.result_of_exp, self.date)