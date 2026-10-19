import time
import random

print("\n")
print("      MINI JOGO SIMULADOR DE FLIP-FLOP D         \n")
print("REGRAS:")
print("1. O valor de D (Entrada) será gerado na tela.")
print("2. O Flip-Flop é salvo apenas quando o CLOCK bate.")
print("3. Quando aparecer 'CLOCK!', digite sua resposta e aperte ENTER")
print("4. Se errar o bit, o sistema falha\n")
print("NOTA: Mini jogo disponível em: https://github.com/jodsv/simulador-flipflop-d")

# LOOP EXTERNO
while True:
    input("\nPressione ENTER para ligar a máquina...")
    print("\nIniciando clock...\n")
    time.sleep(1)

    D = 0 # Valor inicial da entrada
    rodadas = 0

  # LOOP INTERNO
    while True:
        acao = random.choice(['troca', 'troca', 'troca', 'clock'])
        
        if acao == 'troca':
            D = random.choice([0, 1])
            print(f"Entrada D mudou para: [ {D} ]")
            time.sleep(random.uniform(1.0, 2.0))
            
        elif acao == 'clock':
            print("CLOCK!!")
            resposta = input("Qual bit o Flip-Flop deve salvar em Q?: ")
            
            if resposta == str(D):
                rodadas += 1
                print(f"Correto! Saída Q agora armazenou o bit {D}.")
                print(f"Sincronias bem-sucedidas: {rodadas}")
                print("Sistema estável. Continuando...\n")
                time.sleep(2)

            else:
                print(f"O último dado na porta D era {D}, e você tentou salvar {resposta}.")
                print(f"Você sobreviveu a {rodadas} pulsos de clock.")
                print("O SISTEMA FALHOU")
                break # Encerra apenas o loop interno (a rodada)

    tentar_dnv = input("\nDeseja reiniciar o sistema e tentar novamente? (s/n): ").strip().lower()
    
    if tentar_dnv != 's':
        print("Desligando o simulador...")
        break # Encerra o loop externo, fechando o programa de vez
