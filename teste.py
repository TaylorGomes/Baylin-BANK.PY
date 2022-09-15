from models.cliente import Cliente
from models.conta import Conta


Jupira: Cliente = Cliente('Jupira Joana', 'Jupira@gmail.com', '123.456.789-01', '02/08/1957')
angelica: Cliente = Cliente('Angelica Holdingh', 'angelica@gmail.com', '234.567.890-02', '08/05/1988')

# print(felicity)
# print(angelina)

contaf: Conta = Conta(Jupira)
contaa: Conta = Conta(angelica)

# print(contaf)
# print(contaa)

