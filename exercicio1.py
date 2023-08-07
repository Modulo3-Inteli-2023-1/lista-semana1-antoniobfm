#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(x, y):

  # Soma, subtração, multiplicação e divisão de x e y
  soma = x + y
  subtracao = x - y
  multiplicacao = x * y

  # Caso exista divisão por zero, retorne zero.
  if y == 0:
    divisao = 0
  else:
    divisao = x / y

  return soma, subtracao, multiplicacao, divisao
    
# Teste a sua função aqui (caso ache necessário)
print(multiplas_operacoes(10, 0))
