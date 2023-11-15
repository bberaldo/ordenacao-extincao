#Gestão de Dados de Conservação: Desenvolver um sistema que ordena e compara dados de conservação de espécies ameaçadas, como populações de animais ou vegetação nativa, para apoiar esforços de preservação.
import openpyxl

def selectionSort(array):
  for i in range(len(array)):
        
    # setting min_indx equal to the first unsorted element
    
    min_indx = i
    # Loop to iterate over un-sorted sub-array
    for j in range(i+1, len(array)):
    
    #Finding the minimum element in the unsorted sub-array
        if array[min_indx] > array[j]:
            min_indx = j
              
    # swapping the minimum element with the element at min_index to place it at its correct position    
    array[i], array[min_indx] = array[min_indx], array[i]
    
  print(array)

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
  selectionSort(valores)
  print(valores)

# mostrar valores
  for i in range(2, valores + 1):
    print(valores)
     

def menu():
  print("menu:")

  try:
    opcao = int(input("Escolha uma opção"))
  except Exception as e:
    print("Valor inválido. Tente novamente:")

lerDados()