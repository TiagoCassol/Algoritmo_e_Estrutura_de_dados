from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro


if __name__ == "__main__":
    carro = Veiculo(marca="Fiat", qtdRodas=4, modelo="Uno")
    carro.imprimirInformacoes()

    carro.acelerar(50)
    carro.imprimirInformacoes()


    carro.frear(20)
    carro.imprimirInformacoes()

    print("\n")

    bicicleta = Bicicleta(marca="Caloi", qtdRodas=2, modelo="Mountain", numMarchas=18, bagageiro=True)
    bicicleta.imprimirInformacoes()

    bicicleta.acelerar(10)
    bicicleta.imprimirInformacoes()

    bicicleta.frear(5)
    bicicleta.imprimirInformacoes()

    print("\n")

    automovel = Automovel(marca="Honda", qtdRodas=4, modelo="Civic", potenciaDoMotor=12)
    automovel.imprimirInformacoes()

    automovel.acelerar(100)
    automovel.imprimirInformacoes()

    automovel.frear(15)
    automovel.imprimirInformacoes()

    
    print("\n")

    moto = Moto(marca="Honda", qtdRodas=2, modelo="moto", potenciaDoMotor=19,partidaEletrica=True)
    moto.imprimirInformacoes()

    moto.acelerar(50)
    moto.imprimirInformacoes()

    moto.frear(25)
    moto.imprimirInformacoes()

    print("\n")

    carro = Carro(marca="hyundai", qtdRodas=4, modelo="esportivo", potenciaDoMotor=60,qtdPortas=4)
    carro.imprimirInformacoes()

    carro.acelerar(20)
    carro.imprimirInformacoes()

    carro.frear(5)
    carro.imprimirInformacoes()