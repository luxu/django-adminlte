from django.db import models
from . import constants

class Base(models.Model):
    """Base parent model for all the models"""

    created_at = models.DateTimeField("Criado em", auto_now_add=True, null=True)
    modified_at = models.DateTimeField("Atualizado em", auto_now=True, null=True)
    status = models.BooleanField(choices=constants.STATUS, default=constants.ATIVO)

    class Meta:
        abstract = True



class City(Base):
    description = models.CharField(
        "Description",
        max_length=100,
        null=True
    )


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Localidade"
        verbose_name_plural = "Localidades"
        ordering = ["-id"]

class Pecas(Base):
    data = models.DateField(
        verbose_name="Data da Troca",
    )
    veiculo = models.CharField(
        verbose_name="Veículo",
        max_length=1,
        choices=constants.TYPE_VEHICLE
    )
    proxtroca = models.IntegerField(
        verbose_name="Próxima Troca",
        default=1
    )
    troca = models.IntegerField(
        verbose_name="Troca",
        default=1
    )
    city = models.ForeignKey(
        City,
        verbose_name="Cidade",
        on_delete=models.CASCADE,
        default=1,
        null=True,
        blank=True,
    )
    total = models.CharField(
        verbose_name="Total",
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Peça"
        verbose_name_plural = "Peças"
        ordering = ["-id"]


class Itenspecas(models.Model):
    description = models.CharField(
        verbose_name="Descrição",
        max_length=100
    )
    pecas = models.ForeignKey(
        Pecas,
        verbose_name="Peças",
        on_delete=models.PROTECT
    )
    price = models.CharField(
        verbose_name="Preço",
        blank=True,
        null=True,
        max_length=100
    )
    quantity = models.IntegerField(
        verbose_name="Quantidade Comprada",
        default=1
    )
    subtotal = models.CharField(
        verbose_name="Sub-Total",
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Item Peça"
        verbose_name_plural = "Itens Peças"
        ordering = ["-id"]
