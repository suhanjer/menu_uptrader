from django.db import models

# Create your models here.
class Menu0(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, default='1')

    def __str__(self):
        return f"{self.name}"

class Menu1(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, default='1')
    previous = models.ForeignKey(Menu0, on_delete=models.CASCADE, related_name="level1")

    def __str__(self):
        return f"{self.previous} --> {self.name}"

class Menu2(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, default='1')
    previous = models.ForeignKey(Menu1, on_delete=models.CASCADE, related_name="level2")

    def __str__(self):
        return f"{self.previous} --> {self.name}"

class Menu3(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, default='1')
    previous = models.ForeignKey(Menu2, on_delete=models.CASCADE, related_name="level3")

    def __str__(self):
        return f"{self.previous} --> {self.name}"

class Menu4(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, default='1')
    previous = models.ForeignKey(Menu3, on_delete=models.CASCADE, related_name="level4")

    def __str__(self):
        return f"{self.previous} --> {self.name}"