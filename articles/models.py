from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')
    # articles = models.ManyToManyField(Article, related_name = 'tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['name']


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope', through_fields=('article', 'tag'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    if is_main:
        ordering = ['-published_at']
    else:
        ordering = ['name']

    # if is_main:
    #     queryset = Article.objects.order_by('name')
    # else:
    #     queryset = Article.objects.order_by(ordering)