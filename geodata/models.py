from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Region name"), unique=True)
    slug = models.SlugField(max_length=200, blank=True)
    post_code = models.IntegerField(verbose_name=_("Postal code"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(
        max_length=255, verbose_name=_("District name"), unique=True
    )
    slug = models.SlugField(max_length=200, blank=True)

    region = models.ForeignKey(
        to=Region, on_delete=models.CASCADE, related_name="districts"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ward name"))
    slug = models.SlugField(max_length=200, blank=True)
    district = models.ForeignKey(
        to=District, on_delete=models.PROTECT, related_name="wards"
    )
    post_code = models.IntegerField(verbose_name=_("Postal code"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
