# na programaçao existe uma coisa que tem varios nomes

# conversa de tipos, coerção
# type convertion,typecasting, coercion 
# seria basicamente converter um tipo em outro tipo
# quando voce soma 
print(1+1)
# o python reconhece isso como um inteiro e faz a soma 
# quando voce soma
print('a' + 'b')
# python reconhece isso como uma str e concatena
# concatenar significa juntar 2 coisas
# isso se chama polimorfismo ele ta utilisando 1 operador de soma para 2 situaçao pra fazer coisas diferentes
# isso so acontece em linguagens dinamicas
# pq vc passa dois tipos para o interpretador e ele sabe o que fazer com esses 2 tipos
print(('1') + 1)
# o python nao pode fazer pq ele nao concatena uma str com um int

# tipos imutáveis e primitivos:
# str, int, float, bool
# colocando dentro de uma funçao print
print('1', type(1))
# e colocar um valor e o tipo daquele valor o python vai entender que é uma string 
# se a gente quizer fazer que ele vire um inteiro e so colocar um int
print(int('1'), type(int('1')))
# precisa colocar o int nos duas classes para ele saber que fez a coeçao
# se fizermos:
print(int('1') + 1)
# assim ele entende que é um int
# o python vai indentificar essa string como um inteiro e fazer a soma dos dois
# o python tambem pode entende como float se a gente mudar o int pra float
print(type(float('1') + 1))
# assim ele entende que é um float
# sempre que a gente ver um numero com um ponto, podemos indentificar que estamos falando de um float
# quando a gente colocar parentese dentro de parentese o python primeiro vai ler o parentese do meio depois os outros
# tipo assim (terceiro(segundo(priomeiro)))
print(bool(''))
# so tem dois valores True ou False 
# ou seja ele vai indentificar se aquilo é verdadeiro ou falso
# uma funçao com o bolean vazia é False ja uma funçao com a bolean que tem um valor (pode ser um espaço) é True
print(11 + 'b')
# o python nao vai entender que voce esta passando uma str pra ele, ou seja, ele nao vai concatenar esse valor
print(str(11) + 'b')
# pra ele indentificar indentificar esse dois valores em string a gente precisa colocar o str para ele concatenar a string
