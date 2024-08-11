class GerenciadorRegistrosMedicos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GerenciadorRegistrosMedicos, cls).__new__(cls)
            cls._instancia._registros = {}
        return cls._instancia

    def adicionar_registro(self, id_paciente, dados_paciente):
        self._instancia._registros[id_paciente] = dados_paciente

    def obter_registro(self, id_paciente):
        return self._instancia._registros.get(id_paciente)
