import random
import time
from pyscript import document

# Programa python feito por Helena e Antonio para verificar estatisticamente a solucao do paradoxo Monty Hall
# 16-06-2025

def monty_all(event):
  # Numero de vezes que se executa o concurso
  # n = 10000
  # n = int(input("Numero de concursos ( 1000000 ): ") or "1000000")
  input_n = document.querySelector("#concursos")

  if input_n.value == "":
    n = 100000
  else:
    n = int(input_n.value)

  # Numero de vezes que se acertou na porta do carro quando concorrent muda de porta
  acertou_mudandoporta = 0
  # Numero de vezes que se acertou na porta do carro quando concorrent não muda de porta
  acertou_mantendoporta = 0

  start = time.time()

  for i in range(n):
  
    # Lista de portas para escolha do Monty
    porta = [ 0, 1, 2]
    # Lista de portas para segunda escolha do concorrente
    escolha_porta = [ 0, 1, 2]
  
    # Define aleatoriamente porta do carro
    carro_porta = random.randint(0,2)
  
    # Define aleatoriamente porta da primeira escolha do concorrente
    primeira_escolha = random.randint(0,2)
  
    porta.remove(primeira_escolha)
    escolha_porta.remove(primeira_escolha)
  
    if carro_porta != primeira_escolha:
      porta.remove(carro_porta)
  
    # Remove porta aberta pelo Monty da lista de escolhas do concorrent
    escolha_porta.remove(porta[0])
  
    # Verifica se concorrente acertou ou não na porta do carro quando escolhe outra porta
    if escolha_porta[0] == carro_porta:
      acertou_mudandoporta = acertou_mudandoporta + 1
  
    # Verifica se concorrente acertou ou não na porta do carro quando mantem a escolha da porta
    if primeira_escolha == carro_porta:
      acertou_mantendoporta = acertou_mantendoporta + 1
  
  end = time.time()

  #print("Numero de concursos", n)
  #print("% media de acertos mudando porta", round(acertou_mudandoporta / n * 100, 3 ) )
  #print("% media de acertos mantendo porta", round( acertou_mantendoporta / n * 100, 3 ) )

  runtime = round(end - start, 4)

  displayText = "\nNumber of shows simulated: " + str(n) + "\n" + "Average of hits changing selected door: " + str(round(acertou_mudandoporta / n * 100, 3 )) + "%" + "\n" + "Average of hits keeping selected door: " + str(round( acertou_mantendoporta / n * 100, 3 )) + "%" + "\n\n" + "Simulation runtime: " + str(runtime) + " (s)"

  output_div = document.querySelector("#output")
  output_div.innerText = displayText