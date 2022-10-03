# Crie uma classe de sua preferência com, no mínimo, uma variável,
# um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.


class Calculo:

    def __init__(self, v, i:int):
        self.valor = v
        self.incremento = i

    def Incrementar(self):
        self.valor = self.valor + self.incremento

a = Calculo(7, 2)
c1 = a.Incrementar()


b = Calculo(8, 2)
c2 = b.Incrementar()

c = Calculo(9, 2)
c3 = c.Incrementar()
print(a.valor, b.valor, c.valor)

