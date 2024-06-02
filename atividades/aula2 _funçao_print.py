print()# a funçao print ela é utilizada para imprimir coisas na tela.
#e ela recebe um argumento, argumento sao coisas que voce passa para funçoes como o print()
print(12, 34)# para separa um srgumento do outro precisa ultilisar as virgulas quando sao 2 argumentos tipo print(12, 34)
print(54, 74)# para separa um srgumento do outro precisa ultilisar as virgulas quando sao 2 argumentos tipo print(12, 34))
# se eu clicar ensima de uma funçao e aperta ctrl c e ctrl v; ele basicamente desse a mesma funçao
print(12, 34, sep="-")# o sep="" serve como um separador
# se vc colocar o sep"-"assim ele vai separar com traços
# o CRLN em baixo do seu editor  especificamente para o windows.
# \r\n siguinifica o r é um return e o \n e um linefit
# \r\n -> CRLF carry an return line feed
# e isso faz com o editor quebre a linha 
# esses dois comandos nao aparece na tela, mas ele queva a linha
print(12, 34, 1011, sep="-", end="\r\n")# o end por padrao e o final da linha
# Print com letra maiuscula nao existe no python