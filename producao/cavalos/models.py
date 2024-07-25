from django.db import models

# Create your models here.

class Cavalos(models.Model):
    frota = models.CharField(max_length=150, verbose_name="Frota")
    placa = models.CharField(max_length=150, verbose_name="Placa")
    motorista = models.CharField(max_length=150, verbose_name="Motorista padrão")
    renavam = models.CharField(max_length=150, verbose_name="Renavam")
    GENDER_CHOICES = (
        ('A', '2024/2024'),
        ('B', '2023/2024'),
        ('C', '2022/2023'),
        ('D', '2021/2022'),
        ('E', '2020/2021'),
        ('F', '2019/2020'),
        ('G', '2018/2019'),
        ('H', '2017/2018'),
    )
    anomod = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Ano / Modelo")
    GENDER_CHOICES = (
        ('B', 'Branco'),
        ('P', 'Preto'),
        ('V', 'Verde'),
        ('V', 'Vermelho'),
    )
    cor = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Cor")
    chassi = models.CharField(max_length=150, verbose_name="Chassi")
    crlv = models.CharField(max_length=150, verbose_name="CRLV")
    GENDER_CHOICES = (
        ('D', 'DAF'),
        ('S', 'Scania'),
        ('V', 'Volvo'),
    )
    marca = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Marca")
    GENDER_CHOICES = (
        ('R', 'R 450'),
        ('F', 'FH 460'),
        ('F', 'FH 540'),
    )
    modelo = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Modelo")
    GENDER_CHOICES = (
        ('M', 'Mecânica'),
        ('P', 'Pneumática'),
    )
    suspensao = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Suspensão")
    GENDER_CHOICES = (
        ('2', '6x2'),
        ('4', '6x4'),
    )
    tracao = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Tração")
    altura = models.CharField(max_length=150, verbose_name="Altura")
    capdiesel = models.CharField(max_length=150, verbose_name="Cap.Diesel")
    pbt = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="PBT")
    tara = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Tara")
    GENDER_CHOICES = (
        ('A', 'Araucária'),
        ('C', 'Canoas'),
        ('C', 'Cubatão'),
        ('I', 'Itajaí'),
        ('P', 'Paulínia'),
    )
    locado = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Locado")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    macaricoele = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Maçarico eletrônico")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    bombadeasfalto = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bomba de asfalto")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    bombahidraulica = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bomba Hidráulica")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    esperatforca = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Espera T.Força")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    placasolar = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Placa solar")
    GENDER_CHOICES = (
        ('A', 'Agregado'),
        ('O', 'Operação'),
        ('V', 'Vendido'),
    )
    status = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Status")
    GENDER_CHOICES = (
        ('A', 'Antigo cirio'),
        ('M', 'Moderno cirio'),
        ('I', 'Ingomar'),
    )
    bloqueador = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bloqueador")
    GENDER_CHOICES = (
        ('A', 'VIA AVANT'),
        ('D', 'VIA DUPLA'),
        ('G', 'GOTTA LTDA'),
        ('R', 'MR LTDA'),
        ('R', 'R.J.M Andrade'),
    )
    transportadora = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Transportadora")
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    notafiscal = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Nota fiscal")
    GENDER_CHOICES = (
        ('F', 'FMS'),
        ('G', 'GPS'),
        ('M', 'MAXTRACK'),
        ('T', 'TAC'),
    )
    velocidade = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Velocidade")
    fimdegarantia = models.CharField(max_length=150, verbose_name="Fim De Garantia (Altere a data!)", default="00/00/2024")  # Valor padrão adicionado
    dataentregatecnica = models.CharField(max_length=150, verbose_name="Data Entrega Técnica (Altere a data!)", default="00/00/2024")  # Valor padrão adicionado


    def __str__(self):
        return f"{self.placa} "