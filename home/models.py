# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Empresa(models.Model):

    #__Empresa_FIELDS__
    nombre_empresa = models.CharField(max_length=255, null=True, blank=True)
    id_empresa = models.IntegerField(null=True, blank=True)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")


class Estado_Tecnico(models.Model):

    #__Estado_Tecnico_FIELDS__
    estado_tecnico = models.TextField(max_length=255, null=True, blank=True)
    id_estado_tecnico = models.IntegerField(null=True, blank=True)

    #__Estado_Tecnico_FIELDS__END

    class Meta:
        verbose_name        = _("Estado_Tecnico")
        verbose_name_plural = _("Estado_Tecnico")


class Marca(models.Model):

    #__Marca_FIELDS__
    marca_equipo = models.TextField(max_length=255, null=True, blank=True)
    id_marca_equipo = models.IntegerField(null=True, blank=True)

    #__Marca_FIELDS__END

    class Meta:
        verbose_name        = _("Marca")
        verbose_name_plural = _("Marca")


class Modelo(models.Model):

    #__Modelo_FIELDS__
    id_modelo = models.IntegerField(null=True, blank=True)
    nombre_modelo = models.CharField(max_length=255, null=True, blank=True)
    id_marca_equipo = models.ForeignKey(Marca, on_delete=models.CASCADE)

    #__Modelo_FIELDS__END

    class Meta:
        verbose_name        = _("Modelo")
        verbose_name_plural = _("Modelo")


class Rodaje(models.Model):

    #__Rodaje_FIELDS__
    tipo_rodaje = models.TextField(max_length=255, null=True, blank=True)
    id_rodaje = models.IntegerField(null=True, blank=True)

    #__Rodaje_FIELDS__END

    class Meta:
        verbose_name        = _("Rodaje")
        verbose_name_plural = _("Rodaje")


class Tipo_Equipo(models.Model):

    #__Tipo_Equipo_FIELDS__
    id_tipo_equipo = models.IntegerField(null=True, blank=True)

    #__Tipo_Equipo_FIELDS__END

    class Meta:
        verbose_name        = _("Tipo_Equipo")
        verbose_name_plural = _("Tipo_Equipo")


class Ueb(models.Model):

    #__Ueb_FIELDS__
    nombre_empresa = models.TextField(max_length=255, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    #__Ueb_FIELDS__END

    class Meta:
        verbose_name        = _("Ueb")
        verbose_name_plural = _("Ueb")


class Equipo_Minero(models.Model):

    #__Equipo_Minero_FIELDS__
    tipo = models.ForeignKey(Tipo_Equipo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ueb = models.ForeignKey(UEB, on_delete=models.CASCADE)
    rodaje = models.ForeignKey(Rodaje, on_delete=models.CASCADE)
    estado_tecnico = models.ForeignKey(Estado_Tecnico, on_delete=models.CASCADE)
    año_fabricacion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    capacidad = models.IntegerField(null=True, blank=True)
    vin = models.CharField(max_length=255, null=True, blank=True)
    numero_chasis = models.TextField(max_length=255, null=True, blank=True)
    numero_motor = models.TextField(max_length=255, null=True, blank=True)
    potencia_motor = models.IntegerField(null=True, blank=True)
    altura_maxima = models.IntegerField(null=True, blank=True)
    arrendado = models.CharField(max_length=255, null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)

    #__Equipo_Minero_FIELDS__END

    class Meta:
        verbose_name        = _("Equipo_Minero")
        verbose_name_plural = _("Equipo_Minero")



#__MODELS__END
