#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(numeros):
  # Crie uma variável para armazenar a soma
  soma = 0
  
  # Para cada número na lista de números
  for numero in numeros:
    # Se o número for uma lista, some o resultado da função soma_dos_aninhados
    if isinstance(numero, list):
      soma += soma_dos_aninhados(numero)
    # Caso contrário, some o número
    else:
      soma += numero
  
  # Retorne a soma
  return soma

# Teste a sua função aqui (caso ache necessário)
print(soma_dos_aninhados([1, 2, [3, 4, [15, 6]]]))











