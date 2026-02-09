from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')
    # articles = models.ManyToManyField(Article, related_name = 'tags')



class Article(models.Model):
    count = 0
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    tags = models.ManyToManyField(Tag, through='Scope')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    count += 1
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)
