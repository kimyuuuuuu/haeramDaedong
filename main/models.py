from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainPhoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # 게시글의 제목(postname)으로 Post Object 대신하기
    def __str__(self):
        return self.postname
