from django.db import models
from .validators import *


# Create your models here.


class Exp(models.Model):
    expression = models.CharField('expression', max_length=150, db_index=True,
                                  validators=[
                                              check_char_in_string,
                                              check_expression,
                                              check_if_floordiv
                                              ])
    result_of_expression = models.CharField('result of expression', max_length=150, db_index=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    expressions = models.Manager()

    def __str__(self):
        return '{} {} {}'.format(self.expression, self.result_of_expression, self.date)
