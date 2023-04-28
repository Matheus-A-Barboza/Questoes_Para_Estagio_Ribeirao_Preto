# Escreva um programa que inverta os caracteres de um string.
# Evite usar funções prontas, como, por exemplo, reverse; 

palavra = input('Digite uma palavra para inverter: ')

palavra_invertida = ''.join(list(palavra)[::-1])

print(palavra_invertida)