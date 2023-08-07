#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(x, y):

  # Se y for igual a 0, retorne 0
  if y == 0:
    return 0

  # Caso contrário, retorne a soma, subtração, multiplicação e divisão de x e y
  soma = x + y
  subtracao = x - y
  multiplicacao = x * y
  divisao = x / y

  return soma, subtracao, multiplicacao, divisao
    
# Teste a sua função aqui (caso ache necessário)
print(multiplas_operacoes(10, 2))
