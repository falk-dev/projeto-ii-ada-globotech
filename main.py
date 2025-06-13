# Importa a classe de orquestração que gerencia toda a lógica do sistema
from orquestracao.orquestracao import SistemaAnaliseEngajamento

# Função principal que roda o sistema
def main():
    # Caminho do CSV
    caminho_csv = "interacoes_globo.csv"

    # Instancia o sistema
    sistema = SistemaAnaliseEngajamento()

    # Carrega e processa os dados do CSV
    sistema.processar_interacoes_do_csv(caminho_csv)

    # Loop de menu interativo
    while True:
        print("\nMenu de opções:\n")
        print("1. Listar plataformas cadastradas")
        print("2. Listar conteúdos cadastrados")
        print("3. Visualizar contagem por tipo de interação")
        print("4. Visualizar total de comentários por conteúdo")
        print("5. Relatório de engajamento por conteúdo")
        print("6. Relatório de atividade dos usuários")
        print("7. Top 5 conteúdos por tempo total de consumo")
        print("8. Sair")

        # Recebe a opção do usuário
        opcao = input("\nDigite a opção desejada: ")

       # Gera os relatórios
        if opcao == "1":
            # Lista todas as plataformas cadastradas
            plataformas = sistema_analise.listar_plataformas()
            print("\n📡 Plataformas cadastradas:")
            for p in plataformas:
                print("-", p)

        elif opcao == "2":
            # Lista todos os conteúdos registrados
            conteudos = list(sistema_analise._SistemaAnaliseEngajamento__conteudos_registrados.values())
            print("\n🎬 Conteúdos cadastrados:")
            for c in conteudos:
                print(c)

        elif opcao == "3":
            # Mostra a contagem de interações por tipo para cada conteúdo
            conteudos = list(sistema_analise._SistemaAnaliseEngajamento__conteudos_registrados.values())
            print("\n📊 Contagem por tipo de interação: \n")
            for c in conteudos:
                contagem = c.calcular_contagem_por_tipo_interacao()
                print(f"➡️  {c.nome_conteudo}")
                for tipo, qtde in contagem.items():
                    simbolo = {
                        "view_start": "👀",
                        "like": "❤️",
                        "comment": "💬",
                        "share": "🤝"
                    }.get(tipo, "➕")
                    print(f"  {simbolo}  {tipo}: {qtde}")
                print("---------------------------------------")

        elif opcao == "4":
            # Mostra os comentários feitos para cada conteúdo
            conteudos = list(sistema_analise._SistemaAnaliseEngajamento__conteudos_registrados.values())
            print("\n💬 Total de comentários por conteúdo: \n")
            for c in conteudos:
                comentarios = c.listar_comentarios()
                if comentarios:
                    print(f"Comentários do conteúdo {c.id_conteudo}: {c.nome_conteudo}")
                    print(f"Total de comentários: {len(comentarios)}")
                    for comentario in comentarios:
                        print(f"- {comentario}")
                    print()
                else:
                    print(f"{c.nome_conteudo} - Sem comentários.\n")

        elif opcao == "5":
            # Gera relatório com o total de interações por conteúdo
            print("\n📊 Relatório de Engajamento por Conteúdo:")
            sistema.gerar_relatorio_engajamento_conteudos()

        elif opcao == "6":
            # Gera relatório com o número de interações por usuário
            print("\n👥 Relatório de Atividade dos Usuários:")
            sistema.gerar_relatorio_atividade_usuarios()

        elif opcao == "7":
            # Mostra os top 5 conteúdos com maior tempo de consumo
            print("\n🏆 Top 5 Conteúdos por Tempo Total de Consumo:")
            sistema.identificar_top_conteudos(metrica="tempo_total_consumo", n=5)

        elif opcao == "8":
            # Sai do programa
            print("Saindo...")
            break

        else:
            # Opção inválida digitada
            print("Opção inválida. Tente novamente.")

# Ponto de entrada principal do script
if __name__ == "__main__":
    main()