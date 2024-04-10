from Conta import Conta

# c = Conta()
# print("Saldo: ",c.getSaldo())
# c.setSaldo(100)
# print("Saldo: ",c.getSaldo())

c1 = Conta()
print("Saldo: ", c1.saldo)
c1.saldo = 100
print("Saldo: ", c1.saldo)

c1.sacar(98)
c1.depositar(1.5)
print(f'saldo: {c1.sald:.2f}')