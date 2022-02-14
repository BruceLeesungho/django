from django.db import models
from .validators import validate_no_hash, validate_no_numbers, validate_score
from django.core.validators import MinLengthValidator

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, validators = [validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=80, validators = [validate_no_hash, validate_no_numbers])
    score = models.IntegerField(validators = [validate_score])
    dt_created = models.DateField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True,
                                error_messages={'unique': '이미 있는 제목이네요!'})
    content = models.TextField(validators = [MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.') 
    ])
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
