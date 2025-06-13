from orquestracao.orquestracao import SistemaAnaliseEngajamento

def main():
    # Caminho do CSV
    caminho_csv = "interacoes_globo.csv"

    # Instancia o sistema
    sistema = SistemaAnaliseEngajamento()

    # Carrega e processa os dados do CSV
    sistema.processar_interacoes_do_csv(caminho_csv)

    # Gera os relatórios (valeu Will pela ideia dos emojis no projeto 1 kkkk)
    print("\n📊 Relatório de Engajamento por Conteúdo:")
    sistema.gerar_relatorio_engajamento_conteudos()

    print("\n👥 Relatório de Atividade dos Usuários:")
    sistema.gerar_relatorio_atividade_usuarios()

    print("\n🏆 Top 5 Conteúdos por Tempo Total de Consumo:")
    sistema.identificar_top_conteudos(metrica="tempo_total_consumo", n=5)

if __name__ == "__main__":
    main()