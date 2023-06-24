class bank:

    def __init__(self):
        self.saldo = 0.0
        self.acoes = []
        self.flag = 0

    def saque(self,dinheiro):
        if dinheiro < self.saldo and self.flag < 3 and dinheiro <= 500:
            self.saldo = self.saldo - dinheiro
            self.flag += 1
            self.acoes.append(("-", dinheiro))
        else:
            print("Não é possivel sacar esse valor")

    def deposito(self, dinheiro):
        if dinheiro > 0:
            self.saldo = self.saldo + dinheiro
            self.acoes.append(("+", dinheiro))
        else:
            print("Não é permitido depositar valores negativos")

    def extrato(self):
        for ope, val in self.acoes:
            print("Seu extrato: " + ope + " " + str(val))
        print("Seu saldo é: R$ " + str(self.saldo))

print("Digite 1 para Depositar")
print("Digite 2 para Sacar")
print("Digite 3 para Visualizar")
print("Digite -1 para Sair")

sel = 0
banco = banck()

while sel != -1:
    sel = int(input("Digite sua operação: "))
    if sel == 1:
        dim = float(input("Digite o valor que deseja depositar: "))
        banco.deposito(dim)
    elif sel == 2:
        dim = float(input("Digite o valor que deseja sacar: "))
        banco.saque(dim)
    elif sel == 3:
        banco.extrato()
    else:
        print("Operação invalida!")