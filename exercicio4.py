#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
  # Crie uma lista vazia
  lista_duplicados = []
  
  # Para cada item na lista
  for item in lista:
    # Se o item aparecer mais de uma vez na lista
    if lista.count(item) > 1:
      # Adicione o item na lista de duplicados
      lista_duplicados.append(item)
  
  # Se a lista de duplicados tiver algum item
  if len(lista_duplicados) > 0:
    # Retorne True
    return True
  # Caso contrário
  else:
    # Retorne False
    return False

# Teste a sua função aqui (caso ache necessário)
print(tem_duplicados([1, 2, 3, 4, 5, 5]))








