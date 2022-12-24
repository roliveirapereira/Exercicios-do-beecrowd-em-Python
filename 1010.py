cj = input(). split()
produto1 = int(cj[0])
unidadep1 = int(cj[1])
valorp1 = float(cj[2])

jc = input() .split()
produto2 = int(jc[0])
unidadep2 = int(jc[1])
valorp2 = float(jc[2])

totalp1 = unidadep1 * valorp1
totalp2 = unidadep2 * valorp2

total = totalp1 + totalp2

print(f'VALOR A PAGAR: R$ {total:.2f}')

#se for colocar seu codigo coloque com #