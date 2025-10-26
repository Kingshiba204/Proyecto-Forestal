from django.db import models
from django.contrib.auth.models import User

class Predio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Predio")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación")
    superficie = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Superficie (ha)", default=0.0)
    tipo_suelo = models.CharField(max_length=100, verbose_name="Tipo de Suelo", default="No especificado")
    
    class Meta:
        verbose_name = "Predio"
        verbose_name_plural = "Predios"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.ubicacion})"

class Faena(models.Model):
    ESTADO_CHOICES = [
        ('programada', 'Programada'),
        ('en_ejecucion', 'En Ejecución'),
        ('suspendida', 'Suspendida'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Faena")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Término")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE, verbose_name="Predio")
    operario_asignado = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Operario Asignado"
    )

    class Meta:
        ordering = ['fecha_inicio', 'estado']

    def __str__(self):
        return f"{self.nombre} ({self.predio})"
