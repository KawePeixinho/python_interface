from tv import *

tv = televisor('TOSHIBA','TOSHIBA-323')

controle = ControleRemoto(tv)

controle.sintonizaCanal('Globo')
controle.trocaCanal('Globo')

print(tv.canal_atual)