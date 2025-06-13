from analise import SistemaAnaliseEngajamento

sistema_analise = SistemaAnaliseEngajamento()

# Caminho do .csv
arquivo = "interacoes_globo.csv"

# Passando para o método de processamento de interações o arquivo csv.
sistema_analise.processar_interacoes_do_csv(arquivo)

while True:
    print("1. Listar plataformas cadastradas")
    print("2. Listar conteúdos cadastrados")
    print("3. Visualizar contagem por tipo de interação")
    print("4. Visualizar total de comentários por conteúdo")
    print("5. Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        plataformas = sistema_analise.listar_plataformas()

        for p in plataformas:
            print(p)

    elif opcao == "2":
        conteudos = sistema_analise.listar_conteudos()

        for c in conteudos:
            print(c)
            
    elif opcao == "3":
            conteudos = sistema_analise.listar_conteudos()
            print("\n📊 Contagem por tipo de interação: \n")
            for c in conteudos:
                contagem = c.calcular_contagem_por_tipo_interacao()
                print(f"➡️  {c.nome_conteudo}")
                for tipo, qtde in contagem.items():
                    if tipo == "view_start":
                        print(f"  👀  {tipo}: {qtde}")
                    elif tipo == "like":
                        print(f"  ❤️   {tipo}: {qtde}")
                    elif tipo == "comment":
                        print(f"  💬  {tipo}: {qtde}")
                    elif tipo == "share":
                        print(f"  🤝  {tipo}: {qtde}")
                print("---------------------------------------")

    elif opcao == "4":
            conteudos = sistema_analise.listar_conteudos()
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
            print("Saindo...")
            break

    else:
            print("Opção inválida. Tente novamente.")
