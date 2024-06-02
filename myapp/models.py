from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        db_index=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    # image = models.CharField(max_length=30)
    image = models.ImageField(upload_to="blogs")
    # description = models.TextField()
    description = RichTextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        db_index=True,
        editable=False,
    )
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE) # category silinse blogda silinecek
    # category_id = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL) # category-e aid blog-a Null deyeri menimsedilecek

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
