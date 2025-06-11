import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath('entidades')))
module_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(module_path, '..'))

# Adjust the path to import from the parent directory
from entidades.plataforma import Plataforma

class PlataformaTest(unittest.TestCase):

    def test_plataforma(self):
        """ Teste do construtor da classe Plataforma """
        p = Plataforma(1, "Globoplay")
        self.assertEqual(p.id_plataforma, 1)
        self.assertEqual(p.nome_plataforma, "Globoplay")
        
    def test_nome_plataforma_setter_valido(self):
        """ Teste do setter de nome_plataforma """
        p = Plataforma(1, "G1")
        p.nome_plataforma = "GE"
        self.assertEqual(p.nome_plataforma, "GE")
        
    def test_nome_plataforma_vazio(self):
        """ Teste do setter de nome_plataforma com valor vazio """
        with self.assertRaises(ValueError):
            Plataforma(1, "")

    def test_plataforma_eq_hash(self):
        """ Teste de igualdade e hash da classe Plataforma """
        p1 = Plataforma(1, "Globoplay")
        p2 = Plataforma(1, "Globoplay")
        self.assertEqual(p1, p2)
        self.assertEqual(hash(p1), hash(p2))
        plataformas = {p1}
        self.assertIn(p2, plataformas)
    
    def test_repr_str(self):
        """ Teste das representações de string e repr da classe Plataforma """
        p = Plataforma(1, "G1")
        self.assertIn("G1", str(p))
        self.assertIn("G1", repr(p))
        
    def test_lt_comparacao_nome(self):
        p1 = Plataforma(1, "Globo")
        p2 = Plataforma(2, "Globoplay")
        self.assertTrue(p1 < p2)

    def test_lt_comparacao_nome_igual(self):
        p1 = Plataforma(1, "Globo")
        p2 = Plataforma(2, "Globo")
        self.assertFalse(p1 < p2)

    def test_lt_comparacao_nome_maior(self):
        p1 = Plataforma(1, "Globoplay")
        p2 = Plataforma(2, "Globo")
        self.assertFalse(p1 < p2)

    def test_lt_comparacao_com_objeto_diferente(self):
        p1 = Plataforma(1, "Globo")
        obj = object()
        with self.assertRaises(NotImplementedError):
            p1 < obj
        
if __name__ == '__main__':
    unittest.main()