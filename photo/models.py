from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') #User 객체(상위 객체)에서 관련된 하위 객체를 가져올 때 사용함
    
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png') #photo객체가 저장될 위치 및 디폴트 이미지 지정
    
    text = models.TextField() #문자열에 대한 길이 제한 없음
    
    created = models.DateTimeField(auto_now_add=True) #객체에 추가될 때만 자동으로 현재 일시 설정
    
    updated = models.DateTimeField(auto_now=True) #객체가 수정될 때마다 자동으로 현재 일시 설정
    
    class Meta:
        ordering = ['-updated'] #Photo객체를 수정 일시의 내림차순으로 정렬
        
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S") #strftime (string format time)
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)]) #객체의 상세페이지 주소 설정(객체를 추가 또는 수정할 때 이동할 주소, 템플릿 상세화면으로의 주소 등에 쓰임)