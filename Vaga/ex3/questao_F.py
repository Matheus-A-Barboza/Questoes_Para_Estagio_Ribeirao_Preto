# Descubra a lógica e complete o próximo elemento:  

# a) 1, 3, 5, 7, ___  

# b) 2, 4, 8, 16, 32, 64, ____  

# c) 0, 1, 4, 9, 16, 25, 36, ____  

# d) 4, 16, 36, 64, ____  

# e) 1, 1, 2, 3, 5, 8, ____  

# f) 2,10, 12, 16, 17, 18, 19, ____  

# --------------------------------------------------------

# F)

sequencial = [2, 10, 12, 16, 17, 18, 19]
sequencial[0] += 1
sequencial[1] += 2
sequencial[2] += 4
sequencial[3] += 1
sequencial[4] += 1
sequencial[5] += 1
sequencial[6] += 1
prox_num = sequencial[-1]
print(prox_num)

