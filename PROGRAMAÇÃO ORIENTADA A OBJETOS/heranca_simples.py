class Veiculos:
    def __init__(self,cor,placa,rodas):
        self.cor = cor 
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class Motocicleta(Veiculos):
    pass


class Carro(Veiculos):
    pass


class Caminhão(Veiculos):
     def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado

     def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhão("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
