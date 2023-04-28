# Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
# O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão
# de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem
# na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?  

distancia_total = 200
velocidade_carro = 110
velocidade_caminhao = 80
tempo_pedagio = 5/60

velocidade_caminhao_efetiva = velocidade_caminhao - 2 * velocidade_caminhao * tempo_pedagio

tempo = distancia_total / (velocidade_carro + velocidade_caminhao_efetiva)

distancia_carro = velocidade_carro * tempo

distancia_caminhao = distancia_total - distancia_carro

distancia_carro_destino = distancia_total - distancia_carro
distancia_caminhao_destino = distancia_caminhao


if distancia_carro < distancia_caminhao:
    print('O carro estará mais próximo do destino!')
else:
    print('O caminhão estará mais próximo do destino!')
    
# Explicação da Resolução do problema:
# Para resolver este problema, é necessário começar analisando e determinando em que ponto os dois veículos se cruzam na rodovia.
# Podemos fazer isso considerando que, quando os dois veículos se cruzarem, eles terão percorrido uma
# distância total de 100 km (a distância entre as cidades). Sabendo disso, podemos calcular quanto tempo cada veículo
# leva para percorrer essa distância e, em seguida, usar esse tempo para determinar qual veículo está mais próximo
# de Ribeirão Preto no momento do cruzamento.