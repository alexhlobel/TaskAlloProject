from apps.Employees.models import *


class ImageComment(models.Model):
    image_comment = models.ImageField(upload_to='Image')


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image_comment = models.ManyToManyField(ImageComment)

    def __str__(self):
        return self.content[:50]