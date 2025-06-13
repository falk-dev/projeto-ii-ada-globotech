import csv
from datetime import datetime
from entidades.plataforma import Plataforma
from entidades.usuario import Usuario
from entidades.conteudo import Video, Podcast, Artigo
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:
    VERSAO_ANALISE = "2.0"

    def __init__(self):
        self.__plataformas_registradas = {}
        self.__conteudos_registrados = {}
        self.__usuarios_registrados = {}
        self.__proximo_id_plataforma = 1

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        if nome_plataforma in self.__plataformas_registradas:
            return self.__plataformas_registradas[nome_plataforma]
        nova = Plataforma(self.__proximo_id_plataforma, nome_plataforma)
        self.__plataformas_registradas[nome_plataforma] = nova
        self.__proximo_id_plataforma += 1
        return nova

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return self.__plataformas_registradas.get(nome_plataforma) or self.cadastrar_plataforma(nome_plataforma)

    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list:
        with open(caminho_arquivo, encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return [linha for linha in leitor]

    
    def processar_interacoes_do_csv(self, caminho_arquivo: str):
        import csv
        with open(caminho_arquivo, encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                try:
                    id_conteudo = int(linha.get("id_conteudo", 0))
                    nome_conteudo = linha.get("nome_conteudo", "").strip()
                    tipo_conteudo = "video"  # padrão

                    if not nome_conteudo:
                        continue

                    if id_conteudo not in self.__conteudos_registrados:
                        conteudo = Video(id_conteudo, nome_conteudo, duracao_total_video_seg=3600)
                        self.__conteudos_registrados[id_conteudo] = conteudo
                    else:
                        conteudo = self.__conteudos_registrados[id_conteudo]

                    id_usuario = int(linha.get("id_usuario", 0))
                    if id_usuario not in self.__usuarios_registrados:
                        usuario = Usuario(id_usuario)
                        self.__usuarios_registrados[id_usuario] = usuario
                    else:
                        usuario = self.__usuarios_registrados[id_usuario]

                    nome_plataforma = linha.get("plataforma", "").strip()
                    if not nome_plataforma:
                        continue
                    plataforma = self.obter_plataforma(nome_plataforma)

                    tipo_interacao = linha.get("tipo_interacao", "").strip().lower()
                    if tipo_interacao not in Interacao.TIPOS_INTERACAO_VALIDOS:
                        continue

                    watch_duration = int(float(linha.get("watch_duration_seconds", 0)))
                    comentario = linha.get("comment_text", "").strip()
                    timestamp = linha.get("timestamp_interacao", "").strip()
                    if not timestamp:
                        continue

                    interacao = Interacao(
                        conteudo_associado=conteudo,
                        id_usuario=id_usuario,
                        timestamp_interacao=timestamp,
                        plataforma_interacao=plataforma,
                        tipo_interacao=tipo_interacao,
                        watch_duration_seconds=watch_duration,
                        comment_text=comentario
                    )

                    conteudo.adicionar_interacao(interacao)
                    usuario.registrar_interacao(interacao)

                except Exception as e:
                    print(f"[ERRO] Linha ignorada por erro: {e}\nConteúdo bruto: {linha}")
    
        dados = self._carregar_interacoes_csv(caminho_arquivo)
        for linha in dados:
            try:
                id_conteudo = int(linha.get("content_id", 0))
                nome_conteudo = linha.get("content_name", "").strip()
                tipo_conteudo = linha.get("content_type", "").lower().strip()

                if not nome_conteudo or not tipo_conteudo:
                    continue

                if id_conteudo not in self.__conteudos_registrados:
                    if tipo_conteudo == "video":
                        duracao = int(linha.get("content_total_time", 0))
                        conteudo = Video(id_conteudo, nome_conteudo, duracao)
                    elif tipo_conteudo == "podcast":
                        conteudo = Podcast(id_conteudo, nome_conteudo)
                    elif tipo_conteudo == "artigo":
                        tempo_estimado = int(linha.get("content_total_time", 0))
                        conteudo = Artigo(id_conteudo, nome_conteudo, tempo_estimado)
                    else:
                        continue
                    self.__conteudos_registrados[id_conteudo] = conteudo
                else:
                    conteudo = self.__conteudos_registrados[id_conteudo]

                id_usuario = int(linha.get("user_id", 0))
                if id_usuario not in self.__usuarios_registrados:
                    usuario = Usuario(id_usuario)
                    self.__usuarios_registrados[id_usuario] = usuario
                else:
                    usuario = self.__usuarios_registrados[id_usuario]

                nome_plataforma = linha.get("platform", "").strip()
                if not nome_plataforma:
                    continue
                plataforma = self.obter_plataforma(nome_plataforma)

                tipo_interacao = linha.get("interaction_type", "view_start").strip().lower()
                if tipo_interacao not in Interacao.TIPOS_INTERACAO_VALIDOS:
                    continue

                watch_duration = int(float(linha.get("watch_duration", 0)))
                comentario = linha.get("comment_text", "").strip()
                timestamp = linha.get("timestamp", "")

                interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=timestamp,
                    plataforma_interacao=plataforma,
                    tipo_interacao=tipo_interacao,
                    watch_duration_seconds=watch_duration,
                    comment_text=comentario
                )

                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except Exception as e:
                print(f"[ERRO] Linha ignorada por erro: {e}\nConteúdo bruto: {linha}")


    def gerar_relatorio_engajamento_conteudos(self, top_n: int = None):
        print("\n📊 RELATÓRIO DE ENGAJAMENTO POR CONTEÚDO")
        print("---------------------------------------")
        conteudos = list(self.__conteudos_registrados.values())
        if top_n:
            conteudos = conteudos[:top_n]
        for conteudo in conteudos:
            print(conteudo.calcular_total_interacoes_engajamento())

    def gerar_relatorio_atividade_usuarios(self, top_n: int = None):
        print("\n👥 RELATÓRIO DE ATIVIDADE DOS USUÁRIOS")
        print("---------------------------------------")
        usuarios = list(self.__usuarios_registrados.values())
        if top_n:
            usuarios = usuarios[:top_n]
        for usuario in usuarios:
            print(usuario)

    def identificar_top_conteudos(self, metrica: str, n: int):
        print(f"\n⭐ TOP {n} CONTEÚDOS POR: {metrica.upper()}")
        print("---------------------------------------")
        if metrica not in {"tempo_total", "media"}:
            print("Métrica inválida. Use 'tempo_total' ou 'media'.")
            return

        def chave_tempo_total(c):
            return sum(i.watch_duration_seconds for i in c.interacoes if i.watch_duration_seconds > 0)

        def chave_media(c):
            tempos = [i.watch_duration_seconds for i in c.interacoes if i.watch_duration_seconds > 0]
            return sum(tempos) / len(tempos) if tempos else 0

        chave = chave_tempo_total if metrica == "tempo_total" else chave_media
        ordenados = sorted(self.__conteudos_registrados.values(), key=chave, reverse=True)[:n]

        for conteudo in ordenados:
            print(f"- {conteudo.nome_conteudo} (ID: {conteudo.id_conteudo})")


    def listar_conteudos(self) -> list:
        return list(self.__conteudos_registrados.values())

    def listar_usuarios(self) -> list:
        return list(self.__usuarios_registrados.values())
