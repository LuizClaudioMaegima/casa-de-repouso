from django.db import models

class funcionario (models.Model):

 Nome = models.CharField(max_length=50, null = False,blank= False)
 Sobrenome = models.CharField(max_length=50,null =False,blank = False)
 Registro_Empresa = models.IntegerField()
 Escala_de_trabalho = models.DateField(null = False, blank =False)
    

