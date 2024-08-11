from singleton import GerenciadorRegistrosMedicos
from builder import ConstrutorRelatorioMedico
from adapter import SistemaMonitoramentoAntigo, SistemaMonitoramentoNovo, AdaptadorMonitoramento
from strategy import EstrategiaMedicacao, EstrategiaCirurgia, EstrategiaFisioterapia, ContextoTratamento

def main():
    # Singleton: Gerenciador de Registros Médicos
    print("Testando Padrão Singleton:")
    gerenciador1 = GerenciadorRegistrosMedicos()
    gerenciador2 = GerenciadorRegistrosMedicos()
    print(gerenciador1 is gerenciador2)  # Deve ser True
    
    gerenciador1.adicionar_registro("12345", {"nome": "João da Silva", "diagnostico": "Gripe"})
    print(gerenciador2.obter_registro("12345"))  # Deve mostrar o mesmo registro

    print("\nTestando Padrão Builder:")
    # Builder: Construindo um Relatório Médico
    construtor = ConstrutorRelatorioMedico()
    relatorio = (construtor.adicionar_informacoes_paciente("João da Silva", 45)
                         .adicionar_diagnostico("Hipertensão")
                         .adicionar_prescricao("Medicação XYZ")
                         .construir())
    print(relatorio)

    print("\nTestando Padrão Adapter:")
    # Adapter: Sistemas de Monitoramento
    sistema_antigo = SistemaMonitoramentoAntigo("João da Silva")
    sistema_novo = SistemaMonitoramentoNovo("Maria Souza")

    adaptador1 = AdaptadorMonitoramento(sistema_antigo)
    adaptador2 = AdaptadorMonitoramento(sistema_novo)

    print(adaptador1.monitorar())  # Saída: Monitorando João da Silva usando o sistema antigo.
    print(adaptador2.monitorar())  # Saída: Monitorando Maria Souza usando o sistema novo.

    print("\nTestando Padrão Strategy:")
    # Strategy: Estratégias de Tratamento
    paciente = {"nome": "João da Silva", "condicao": "Lesão"}

    contexto = ContextoTratamento(EstrategiaCirurgia())
    print(contexto.executar_tratamento(paciente))  # Saída: Tratando João da Silva com cirurgia.

    contexto = ContextoTratamento(EstrategiaMedicacao())
    print(contexto.executar_tratamento(paciente))  # Saída: Tratando João da Silva com medicação.

if __name__ == "__main__":
    main()
