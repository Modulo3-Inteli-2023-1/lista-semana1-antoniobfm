#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(numeros):
  # Crie uma lista vazia
  lista = []
  
  # Para cada número na lista de números
  for numero in numeros:
    # Se a lista estiver vazia, adicione o número
    if len(lista) == 0:
      lista.append(numero)
    # Caso contrário, adicione o número somado ao último número da lista
    else:
      lista.append(numero + lista[-1])
  
  # Retorne a lista
  return lista

# Teste a sua função aqui (caso ache necessário)
print(cumulativo([2, 3, 4, 5]))









