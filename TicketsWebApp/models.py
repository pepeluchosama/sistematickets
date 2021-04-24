from django.db import models

# Create your models here.

class Ticket(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    asunto=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=2000)
    solucionado=models.BooleanField(default=False)
    class Meta:
        db_table='ticket'

    def __str__(self):
        return str(self.id)


