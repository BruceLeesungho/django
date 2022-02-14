# 이곳에 작성합니다.
from django.core.exceptions import ValidationError


def validate_no_hash(value):
    if "#" in value:
        raise ValidationError("#이 들어갈 수 없습니다.")
        
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError("숫자가 들어갈 수 없습니다.")
    
def validate_score(value):
    if value > 10 or value < 0:
        raise ValidationError("0부터 10사이의 숫자만 들어갈 수 있습니다.")