from django.db import models

class Post(models.Model):
	# Данные о выкладке поста
	title = models.CharField('Заголовок поста', max_length = 200)
	description = models.TextField('Текст поста')
	author = models.CharField('Имя автора', max_length = 100)
	date = models.DateField('Дата публикации')
	img = models.ImageField('Изображения', upload_to = 'image/%Y')

	def __str__(self):
		return f'{self.title}, {self.author}'

	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'


class Comments(models.Model):
	# Коментарии
	email = models.EmailField()
	name = models.CharField('Имя', max_length = 50)
	text_comments = models.TextField('Текст коментария', max_length = 2000)
	post = models.ForeignKey(Post, verbose_name = 'Публикация', on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.name}, {self.post}'

	class Meta:
		verbose_name = 'Коментарий'
		verbose_name_plural = 'Коментарии'

class Likes(models.Model):
	# лайки (Проверка по IP)
	ip = models.CharField('IP адрес', max_length = 100)
	pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)