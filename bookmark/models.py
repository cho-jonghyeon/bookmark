from django.db import models
from django.urls import reverse
# Create your models here.
# 모델 : 데이터베이스를 SQL없이 사용
# 모델 == 데이블, 모델의 필드 = 테이블의 컬럼 필드의 값 = 레코드의 컬럼 데이터 값

class Bookmark(models.Model): # db 테이블 이름이 Bookmark이다
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') #테이블에 두개의 필드가 존재 한다. site_name, url두가지.
    # 필드의종류가 결정 하는 것.
    # 1. 데이터베이스 컬럼 종류, 제약 사항, Form의 종류, Form의 제약 사항.
    def __str__(self):
        # 객체를 출력 할 때 나타낼 값
        return "이 름 : " + self.site_name + "          ,주 소  : " + self.url


    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])