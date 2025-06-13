import pytest
from entidades.conteudo import Conteudo, Video, Podcast, Artigo

class FakeInteracao:
    def __init__(self, tipo, tempo_consumo_seg=0, comentario=None):
        self.tipo = tipo
        self.tempo_consumo_seg = tempo_consumo_seg
        self.comentario = comentario

def test_adicionar_e_contar_interacoes_e_comentarios():
    c = Conteudo(1, "Teste")
    i1 = FakeInteracao("like")
    i2 = FakeInteracao("comentario", comentario="Ótimo!")
    c.adicionar_interacao(i1)
    c.adicionar_interacao(i2)
    assert c.calcular_total_interacoes_engajamento() == 2
    cont = c.calcular_contagem_por_tipo_interacao()
    assert cont["like"] == 1
    assert cont["comentario"] == 1
    assert c.listar_comentarios() == ["Ótimo!"]

def test_tempo_total_e_media_consumo():
    c = Conteudo(2, "Tempo")
    c.adicionar_interacao(FakeInteracao("play", tempo_consumo_seg=30))
    c.adicionar_interacao(FakeInteracao("play", tempo_consumo_seg=90))
    assert c.calcular_tempo_total_consumo() == 120
    assert c.calcular_media_tempo_consumo() == 60.0

@pytest.mark.parametrize("cls, dur_val, tempos, esperado", [
    (Video, 100, [10, 20], 15.0),
    (Podcast, 120, [15, 45], 25.0),
    (Artigo, 90, [30, 60], 50.0),
])
def test_percentual_medio_assistido(cls, dur_val, tempos, esperado):
    inst = cls(3, "X", dur_val)
    for t in tempos:
        inst.adicionar_interacao(FakeInteracao("play", tempo_consumo_seg=t))
    assert pytest.approx(inst.calcular_percentual_medio_assistido(), rel=1e-3) == esperado

def test_percentual_com_duracao_zero():
    assert Video(4, "Vazio", 0).calcular_percentual_medio_assistido() == 0.0
    assert Podcast(5, "Vazio", 0).calcular_percentual_medio_assistido() == 0.0
    assert Artigo(6, "Vazio", 0).calcular_percentual_medio_assistido() == 0.0
