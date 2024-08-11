class EstrategiaTratamento:
    def tratar(self, paciente):
        pass

class EstrategiaMedicacao(EstrategiaTratamento):
    def tratar(self, paciente):
        return f"Tratando {paciente['nome']} com medicação."

class EstrategiaCirurgia(EstrategiaTratamento):
    def tratar(self, paciente):
        return f"Tratando {paciente['nome']} com cirurgia."

class EstrategiaFisioterapia(EstrategiaTratamento):
    def tratar(self, paciente):
        return f"Tratando {paciente['nome']} com fisioterapia."

class ContextoTratamento:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def executar_tratamento(self, paciente):
        return self.estrategia.tratar(paciente)
