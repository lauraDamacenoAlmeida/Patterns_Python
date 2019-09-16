from impostos import *
class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        if(imposto == 'ISS'):
            imposto_calculado = calcula_ISS(orcamento)
        if(imposto == 'ICMS'):
            imposto_calculado = calcula_ICMS(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = Calculador_de_impostos()
    orcamento = Orcamento(5000)
    calculador.realiza_calculo(orcamento,'ISS')
    calculador.realiza_calculo(orcamento, 'ICMS')
