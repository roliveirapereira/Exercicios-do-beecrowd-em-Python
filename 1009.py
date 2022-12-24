nickname = str(input())
salariodepobre = float(input())
vendas = float(input())

bonuszin = (vendas * 15)/100
salario_de_pobre_so_q_com_bonus = bonuszin + salariodepobre
print(f'TOTAL = R$ {salario_de_pobre_so_q_com_bonus:.2f}')


