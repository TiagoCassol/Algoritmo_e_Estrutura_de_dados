from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila
from Lista import Lista

t1 = Torre("Torre A" , "Rua A, 100" )
t2 = Torre("Torre B" , "Rua B, 200" )
print(" ------------- --------- ")

semVagas = Fila()
apsComVaga = Lista()

ap1 = Apartamento("111-A" , t1)
ap2 = Apartamento("222-A" , t1)
ap3 = Apartamento("333-B" , t2)
ap4 = Apartamento("444-A" , t1)
ap5 = Apartamento("555-B" , t2)
ap6 = Apartamento("666-B" , t2)
ap7 = Apartamento("777-A" , t1)
ap8 = Apartamento("888-B" , t2)
ap9 = Apartamento("999-B" , t2)

semVagas.add( ap1 )
semVagas.add( ap2 )
semVagas.add( ap3 )
semVagas.add( ap4 )
semVagas.add( ap5 )
semVagas.add( ap6 )
semVagas.add( ap7 )
semVagas.add( ap8 )
semVagas.add( ap9 )

print(" ------------- --------- ")
apsComVaga.add(semVagas.remover(1))
print(" ------------- --------- ")
apsComVaga.add(semVagas.remover(2))
print(" ------------- --------- ")
apsComVaga.add(semVagas.remover(3))
print(" ------------- --------- ")
apsComVaga.add(semVagas.remover(4))
print(" ------------- --------- ")
apsComVaga.add(semVagas.remover(5))
print(" ------------- --------- ")

while True:
    print('')
    print('')
    print('==============================')
    print('   __  __  _____  _   _  _   _ ')
    print('  |  \/  ||  ___|| \ | || | | |')
    print('  | \  / || |__  |  \| || | | |')
    print('  | |\/| ||  __| | . ` || | | |')
    print('  | |  | || |___ | |\  || |_| |')
    print('  |_|  |_|\____/ \_| \_|\_____|')
    print('==============================')
    print("1- Cadastrar apartamento")
    print("2- Liberar vaga")
    print("3- Imprimir a lista de apartamentos com vaga")
    print("4- Imprimir a fila de espera")
    print("5- Sair")
    print('==============================')
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        numero = input("Número do apartamento: ")
        ap = Apartamento(numero, t1)
        semVagas.add(ap)
        
    elif opcao == '2':
        nVaga = int(input("Número da vaga liberada: "))
        liberou= apsComVaga.remover(nVaga)
        print(liberou)
        if liberou:
            semVagas.add(liberou)
            apartamento = apsComVaga.add( semVagas.remover( nVaga ) )

    elif opcao == '3':
        apsComVaga.imprimir()
    elif opcao == '4':
        semVagas.imprimir()
    elif opcao == '5':
        print("Fim.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        # ap = semVagas.remover( 1 )
        # # print(" ------------- --------- ")
        # apsComVaga.add( ap )
        # semVagas.add(ap)
        # apsComVaga.remover(1)
        # # print(" ------------- --------- ")
        # apsComVaga.add(semVagas.remover(1))

        # nVaga = int(input("Número da vaga liberada: "))
        # apartamento = apsComVaga.add( semVagas.remover( nVaga ) )
        # if apartamento:
        #     print(f"Apartamento {apartamento.numero} da torre {apartamento.torre.nome} foi removido da fila e recebeu a vaga {nVaga}.")

        # apartamentoRemovido = apsComVaga.remover(nVaga)
        # if apartamentoRemovido:
        #     apartamentoEsperando = semVagas.add(apartamentoRemovido)
        #     apartamentoEsperando = semVagas.remover(nVaga)
        #     if apartamentoEsperando:
        #         apartamentoEsperando.vaga = nVaga
        #         apsComVaga.add(apartamentoEsperando)
        #         print(f"Apartamento {apartamentoEsperando.numero} da torre {apartamentoEsperando.torre.nome} foi removido da fila e recebeu a vaga {nVaga}.")



