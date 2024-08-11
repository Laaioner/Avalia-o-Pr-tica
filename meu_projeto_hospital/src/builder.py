class ConstrutorRelatorioMedico:
    def __init__(self):
        self.relatorio = {}

    def adicionar_informacoes_paciente(self, nome, idade):
        self.relatorio['nome'] = nome
        self.relatorio['idade'] = idade
        return self

    def adicionar_diagnostico(self, diagnostico):
        self.relatorio['diagnostico'] = diagnostico
        return self

    def adicionar_prescricao(self, prescricao):
        self.relatorio['prescricao'] = prescricao
        return self

    def construir(self):
        return self.relatorio
