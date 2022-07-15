from cs50 import get_float

while(True):
      valor = get_float("Valor: ")
      if valor >=0:
           break
centavos = round( (valor*100))   

total = 0
for i in[25,10,5,1]:
      total += centavos // 
      centavos %= i
print(total)
    
