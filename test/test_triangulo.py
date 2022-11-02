import pytest
import src.triangulo.triangulo as triangulo

class Testclass:
    def teste_zero(self):
        assert triangulo.verifica_triangulo(0,0,0) == False
    def teste_lado(self):
        assert triangulo.verifica_triangulo(0, 4, 4) == False
    def teste_triangulo(self):
        assert triangulo.verifica_triangulo(2, 3, 4) == True