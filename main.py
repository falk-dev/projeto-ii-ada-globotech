from analise.sistema import SistemaAnaliseEngajamento

sistema_analise = SistemaAnaliseEngajamento()
arquivo = "interacoes_globo.csv"
sistema_analise.processar_interacoes_do_csv(arquivo)

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Listar plataformas cadastradas")
    print("2. Listar conteúdos cadastrados")
    print("3. Comentários por conteúdo")
    print("4. Relatório de engajamento dos conteúdos")
    print("5. Relatório de atividade dos usuários")
    print("6. Visualizar métricas de tempo total de visualização por conteúdo")
    print("7. Visualizar métricas de média de tempo de visualização por conteúdo")
    print("8. Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        plataformas = sistema_analise.listar_plataformas()
        print("\n🌐 Plataformas registradas:")
        for p in plataformas:
            print("-", p)

    elif opcao == "2":
        conteudos = sistema_analise.listar_conteudos()
        print("\n🎬 Conteúdos cadastrados:")
        for c in conteudos:
            print("-", c)

    elif opcao == "3":
        conteudos = sistema_analise.listar_conteudos()
        print("\n💬 Comentários por conteúdo:")
        for c in conteudos:
            print(c.listar_comentarios())

    elif opcao == "4":
        sistema_analise.gerar_relatorio_engajamento_conteudos()

    elif opcao == "5":
        sistema_analise.gerar_relatorio_atividade_usuarios()

    elif opcao == "6":
            print("\n⏱️  Tempo total de visualização por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.calcular_tempo_total_consumo()
                    print(relatorio)

    elif opcao == "7":
            print("\n⏱️  Média de tempo de visualização por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.calcular_media_tempo_consumo()
                    print(relatorio)

    elif opcao == "8":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
