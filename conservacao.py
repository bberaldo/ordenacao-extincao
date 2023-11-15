#Gestão de Dados de Conservação: Desenvolver um sistema que ordena e compara dados de conservação de espécies ameaçadas, como populações de animais ou vegetação nativa, para apoiar esforços de preservação.
import openpyxl
import tkinter as tk
import time

def insertionSort(a):
    start_time = time.time()

    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

    end_time = time.time()
    elapsed_time = end_time - start_time
    return a, elapsed_time

def particao(A, esquerda, direita):
    # 1. Seleção do pivô. O pivô será o elemento A[esquerda].
    pivo = A[esquerda]
    # Particionamento do arranjo.
    i = esquerda
    j = direita
    while i <= j:
        # Encontra elemento maior que o pivo.
        while A[i] <= pivo:
            i += 1
            if i == direita:
                break

        # Encontra elemento menor que o pivo.
        while pivo <= A[j]:
            j -= 1
            if j == esquerda:
                break

        # Ponteiros i e j se cruzaram.
        if i >= j:
            break

        # Troca elementos encontrados acima de lugar.
        A[i], A[j] = A[j], A[i]

    # Coloca o pivo no lugar certo.
    pivo, A[j] = A[j], pivo

    # j é o índice em que o pivo agora está.
    return j

def quicksort(A):
  start_time = time.time()

  if len(A) == 0:
      result = A
  else:
      pivot = A[0]
      frente = quicksort([menor for menor in A[1:] if menor <= pivot])
      tras = quicksort([maior for maior in A[1:] if maior > pivot])
      result = frente + [pivot] + tras

  end_time = time.time()
  elapsed_time = end_time - start_time
  return result, elapsed_time

def lerDados():
  try:
    wb_obj = openpyxl.load_workbook("dados.xlsx")
  except Exception as e:
    print(f'Erro: {e}')
  sheet_obj = wb_obj.active
  nRow = sheet_obj.max_row
  
  valores=[]
  for i in range(2, nRow + 1):
    cell_obj = sheet_obj.cell(row = i, column = 6)
    valores.append(cell_obj.value)
  
  print(valores)
  return valores
  # for i in range(len(valores)):
  #    print(valores[i])     

def menu():
  print("menu:")

  try:
    opcao = int(input("Escolha uma opção"))
  except Exception as e:
    print("Valor inválido. Tente novamente:")

def actionBtnQuickSort():
  array = lerDados()
  dados_ordenados, tempo_quick = quicksort(array)
  saidaQuickSort.insert(tk.END, f"Tempo do QuickSort: {tempo_quick:.6f} segundos\n")
  saidaQuickSort.insert(tk.END, f"Dados Ordenados pelo QuickSort: {dados_ordenados}\n")

def actionBtnInsertionSort():
  array = lerDados()
  dados_ordenados, tempo_insertion = insertionSort(array)
  saidaInsertionSort.insert(tk.END, f"Tempo do InsertionSort: {tempo_insertion:.6f} segundos\n")
  saidaInsertionSort.insert(tk.END, f"Dados Ordenados pelo InsertionSort: {dados_ordenados}\n")

# variáveis globais de tempo de cada algoritmo
# criando a janela
janela = tk.Tk()
janela.title("Algorítmos de Ordenação")
janela.geometry("600x400")

# Botão Quick Sort
btnQuickSort = tk.Button(janela, text="QuickSort", command=actionBtnQuickSort)
btnQuickSort.grid(row=1, column=0)

# Botão Insertion Sort
btnInsetionSort = tk.Button(janela, text="InsertionSort", command=actionBtnInsertionSort)
btnInsetionSort.grid(row=1, column=1)

saidaQuickSort = tk.Listbox(janela, height=300, width=40,)  # Ajuste a altura e largura conforme necessário
saidaQuickSort.grid(row=2, column=0)

saidaInsertionSort = tk.Listbox(janela, height=300, width=40)  # Ajuste a altura e largura conforme necessário
saidaInsertionSort.grid(row=2, column=1)

# Iniciar loop da janela
janela.mainloop()
