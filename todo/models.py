from django.db import models

# Create your models here.
class TodoList(models.Model): #장고에서 선언해 놓은 모델스를 사용하기 위해 클래스 사용
	todo = models.CharField(max_length=30)
	description = models.TextField()
	important = models.BooleanField(default=False)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.todo} [{self.id}]'