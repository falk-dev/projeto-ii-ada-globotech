from analise.sistema import SistemaAnaliseEngajamento

sistema_analise = SistemaAnaliseEngajamento()
arquivo = "interacoes_globo.csv"
sistema_analise.processar_interacoes_do_csv(arquivo)

<<<<<<< HEAD
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
=======
>>>>>>> 1cd63ee321a559c4b0aae46dcdb8677d84fa0424

def main():
    while True:
        print("\nMenu de opções:\n")
        print("1. Listar plataformas cadastradas")
        print("2. Listar conteúdos cadastradas")
        print("3. Visualizar métricas de interação por tipo de todos os conteúdos")
        print("4. Visualizar métricas de tempo total de visualização por conteúdo")
        print("5. Visualizar métricas de média de tempo de visualização por conteúdo")
        print("6. Visualizar comentários por conteúdo")
        print("7. Visualizar relatório de engajamento por conteúdo")
        print("8. Visualizar relatório de atividade dos usuários")
        print("9. Visualizar Top 5 conteúdos por tempo total de consumo")
        print("10. Sair do programa")
        # print("")

<<<<<<< HEAD
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
=======
        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            print(f"\n➡️  Plataformas cadastradas:\n")
            plataformas = sistema_analise.listar_plataformas()

            for p in plataformas:
                print(p)

        elif opcao == "2":
            print(f"\n📺  Conteúdos cadastrados:\n")
            conteudos = sistema_analise.listar_conteudos()

            for c in conteudos:
                print(c)

        elif opcao == "3":
            print("\n📊 Métricas de total de interações por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.calcular_total_interacoes_engajamento()
                    print(relatorio)

        elif opcao == "4":
            print("\n⏱️  Tempo total de visualização por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.calcular_tempo_total_consumo()
                    print(relatorio)

        elif opcao == "5":
            print("\n⏱️  Média de tempo de visualização por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.calcular_media_tempo_consumo()
                    print(relatorio)

        elif opcao == "6":
            print("\n💬  Comentários por conteúdo: \n")

            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = conteudo.listar_comentarios()
                    print(relatorio)

        elif opcao == "7":
            print("\n📊 Relatório de Engajamento por Conteúdo:")
            todos_os_conteudos = sistema_analise.listar_conteudos()

            if not todos_os_conteudos:
                print("Nenhum conteúdo cadastrado para gerar relatório.")
            else:
                for conteudo in todos_os_conteudos:
                    relatorio = sistema_analise.gerar_relatorio_engajamento_conteudos()
                    print(relatorio)

        elif opcao == "8":
            print("\n👥 Relatório de Atividade dos Usuários:")
            sistema_analise.gerar_relatorio_atividade_usuarios()

        elif opcao == "9":
            print("\n🏆 Top 5 Conteúdos por Tempo Total de Consumo:")
            sistema_analise.identificar_top_conteudos(
                metrica="tempo_total_consumo", n=5
            )

        elif opcao == "10":
            print("\nSaindo...")
            break

        elif opcao == "":
            pass

        elif opcao == "":
            pass

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
>>>>>>> 1cd63ee321a559c4b0aae46dcdb8677d84fa0424
