from django.db import models


class Salao(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True)  # Este campo deve existir

    def __str__(self):
        return self.nome


class Servico(models.Model):
    salao = models.ForeignKey(Salao, related_name="servicos", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.IntegerField(help_text="Duração do serviço em minutos")

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    # Outras informações relevantes do cliente

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(
        Cliente, related_name="agendamentos", on_delete=models.CASCADE
    )
    servico = models.ForeignKey(
        Servico, related_name="agendamentos", on_delete=models.CASCADE
    )
    salao = models.ForeignKey(
        Salao, related_name="agendamentos", on_delete=models.CASCADE
    )
    data = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=[("pendente", "Pendente"), ("concluido", "Concluído")],
        default="pendente",
    )

    def __str__(self):
        # Formatar a data sem o fuso horário
        return f"Agendamento de {
            self.servico.nome} para {
                self.cliente.nome} no salão {
                    self.salao.nome} em {
                        self.data.strftime('%Y-%m-%d %H:%M:%S')}"
