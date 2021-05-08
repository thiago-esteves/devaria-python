if __name__ == '__main__':

 def lavarCarro(posicao):

   print(f'Lavando carro na posicao {posicao}...')

 def verificarTemCarroNaFila(posicao):

    if(posicao > 10):
     return False
    else:
     return True

if __name__ == '__main__':

   temCarroNaFila = True
   posicao = 1
   while temCarroNaFila:

     lavarCarro(posicao)
     posicao += 1
     temCarroNaFila = verificarTemCarroNaFila(posicao)
   else:
     print('Terminou de lavar os carros!!!')
