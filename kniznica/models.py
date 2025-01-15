from django.db import models




class Autor(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
class Vydavatel(models.Model):
    nazov = models.CharField(max_length=50)

    def __str__(self):
        return self.nazov


class Miesto(models.Model):
    nazov = models.CharField(max_length=50)

    def __str__(self):
        return self.nazov
    

class Kniha(models.Model):
    nazov = models.CharField(max_length=20)
    rok_vydania = models.IntegerField() 
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    vydavatel = models.ForeignKey(Vydavatel, on_delete=models.SET_NULL, null=True, blank=True)
    miesto = models.ForeignKey(Miesto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Kniha"
        verbose_name_plural = "Knihy"
        ordering = ["nazov"]