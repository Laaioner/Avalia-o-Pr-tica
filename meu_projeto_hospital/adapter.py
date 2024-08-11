class SistemaMonitoramentoAntigo:
    def __init__(self, paciente):
        self.paciente = paciente

    def monitorar(self):
        return f"Monitorando {self.paciente} usando o sistema antigo."

class SistemaMonitoramentoNovo:
    def __init__(self, paciente):
        self.paciente = paciente

    def monitorar(self):
        return f"Monitorando {self.paciente} usando o sistema novo."

class AdaptadorMonitoramento:
    def __init__(self, sistema_monitoramento):
        self.sistema_monitoramento = sistema_monitoramento

    def monitorar(self):
        return self.sistema_monitoramento.monitorar()
