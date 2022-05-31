print("-"*40)
print("Bem-vindo ao calculo de fatorial, digite um valor inteiro positivo")
print("-"*40)
num = int(input('Digite o número: '))
fatorial=1
for numero in range(1,num+1):
    fatorial*= numero
print ('O fatorial de', numero, 'e:', fatorial) 