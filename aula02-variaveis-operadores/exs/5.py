# Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro levou para percorrer essa distância?
espaco = 150
vel = 60
horas = espaco//vel # divisão inteira
minutos = espaco % vel # resto


print(f"Um carro leva {horas} horas e {minutos} minutos pra percorrer a distância de {espaco}km a {vel}km/h")
