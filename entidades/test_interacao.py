import pytest
from datetime import datetime

from entidades import Interacao


class Conteudo:
    def __init__(self, id_conteudo, nome_conteudo):
        self._id_conteudo = id_conteudo
        self._nome_conteudo = nome_conteudo

class Plataforma:
    def __init__(self, id_plataforma, nome_plataforma):
        self.__id_plataforma = id_plataforma
        self.__nome_plataforma = nome_plataforma

    @property
    def nome_plataforma(self):
        return self.__nome_plataforma


def test_interacao_criacao_valida(interacao=None):
    conteudo = Conteudo(1, "Teste de Conteúdo")
    plataforma = Plataforma(1, "Globoplay")
    interacao = Interacao(
        id_interacao=100,
        conteudo_associado=conteudo,
        id_usuario=123,
        timestamp_interacao="2024-06-10T22:10:00",
        plataforma_interacao=plataforma,
        tipo_interacao="like",
        watch_duration_seconds=120,
        comment_text="Muito bom!"
    )

    assert interacao.id_interacao == 100
    assert interacao.conteudo_associado._nome_conteudo == "Teste de Conteúdo"
    assert interacao.id_usuario == 123
    assert interacao.plataforma_interacao.nome_plataforma == "Globoplay"
    assert interacao.timestamp_interacao == datetime.fromisoformat("2024-06-10T22:10:00")
    assert interacao.tipo_interacao == "like"
    assert interacao.watch_duration_seconds == 120
    assert interacao.comment_text == "Muito bom!"
    assert interacao.is_engajamento() is True
    assert interacao.is_comentario() is False

def test_interacao_comentario_vazio():
    conteudo = Conteudo(2, "Outro Conteúdo")
    plataforma = Plataforma(2, "G1")
    interacao = Interacao(
        id_interacao=101,
        conteudo_associado=conteudo,
        id_usuario=456,
        timestamp_interacao=datetime(2024, 6, 10, 22, 30),
        plataforma_interacao=plataforma,
        tipo_interacao="comment",
        watch_duration_seconds=0,
        comment_text=""
    )
    assert interacao.is_comentario() is False

def test_interacao_tipo_invalido():
    conteudo = Conteudo(3, "Qualquer")
    plataforma = Plataforma(3, "Gshow")
    with pytest.raises(ValueError):
        Interacao(
            id_interacao=102,
            conteudo_associado=conteudo,
            id_usuario=789,
            timestamp_interacao="2024-06-10T23:00:00",
            plataforma_interacao=plataforma,
            tipo_interacao="download",   # Não permitido!
            watch_duration_seconds=50,
            comment_text="Tentativa de tipo inválido"
        )

# Opcional: testar string e repr
def test_interacao_str_repr():
    conteudo = Conteudo(4, "Conteúdo X")
    plataforma = Plataforma(4, "Globoplay")
    interacao = Interacao(
        id_interacao=103,
        conteudo_associado=conteudo,
        id_usuario=321,
        timestamp_interacao="2024-06-10T23:10:00",
        plataforma_interacao=plataforma,
        tipo_interacao="share"
    )
    assert "share" in str(interacao)
    assert "Conteúdo X" in repr(interacao)
