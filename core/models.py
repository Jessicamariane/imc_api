from django.db import models


class People(models.Model):
    name = models.CharField("nome", max_length=120, blank=False, null=False)
    email = models.EmailField("email", max_length=120, blank=False, null=False)
    height = models.IntegerField(
        "altura", default=0, blank=False, null=False)
    weight = models.IntegerField(
        "peso", default=0, blank=False, null=False)

    @property
    def imc(self):
        return self.weight/self.height

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        get_latest_by = "pk"
        ordering = ['-pk']

    def __str__(self):
        return self.name
