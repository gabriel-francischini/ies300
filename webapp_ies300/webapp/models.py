from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=1024)
    razao_social = models.CharField(max_length=1024)
    nome_fantasia = models.CharField(max_length=1024)

class Mercadoria(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=1024)
    marca = models.CharField(max_length=1024)
    desc = models.TextField()
    codigo_de_barras = models.CharField(max_length=1024)
    qtd_estoque = models.DecimalField(max_digits=3+9+4, decimal_places=4)
    preco = models.DecimalField(max_digits=20+16, decimal_places=16)

class Cliente(models.Model):
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=1024)
    endereco = models.CharField(max_length=1024)
    telefone = models.CharField(max_length=1024)




class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    desc = models.TextField()

class CategoriasDaMercadoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)




class OrdemDeCompra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    desc = models.TextField()
    nota_fiscal = models.CharField(max_length=1024)
    data_hora = models.DateTimeField(null=True)
    data_hora_bd_add = models.DateTimeField(auto_now_add=True)

class ItemNaCompra(models.Model):
    ordem = models.ForeignKey(OrdemDeCompra, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    qtd = models.DecimalField(max_digits=2+9+4, decimal_places=4)
    preco_unidade = models.DecimalField(max_digits=20+16, decimal_places=16)




class OrdemDeVenda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    desc = models.TextField()
    nota_fiscal = models.CharField(max_length=1024)
    data_hora = models.DateTimeField(null=True)
    data_hora_bd_add = models.DateTimeField(auto_now_add=True)

class ItemNaVenda(models.Model):
    ordem = models.ForeignKey(OrdemDeVenda, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    qtd = models.DecimalField(max_digits=2+9+4, decimal_places=4)
    preco_unidade = models.DecimalField(max_digits=20+16, decimal_places=16)




class Manipulacao(models.Model):
    nome = models.CharField(max_length=1024)
    desc = models.TextField()
    data_hora = models.DateTimeField()
    data_hora_bd = models.DateTimeField(auto_now_add=True)

class ManipulacaoInsumo(models.Model):
    manipulacao = models.ForeignKey(Manipulacao, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    qtd = models.DecimalField(max_digits=2+9+4, decimal_places=4)

class ManipulacaoResultado(models.Model):
    manipulacao = models.ForeignKey(Manipulacao, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    qtd = models.DecimalField(max_digits=2+9+4, decimal_places=4)
