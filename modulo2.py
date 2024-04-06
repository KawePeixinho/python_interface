class primeira_classe:  #criando a classe primeira_classe
    'minha primeira classe criada, no curso de interface grafica na fundação bradesco' #docstring para exibir ela, utiliza o metodo __doc__

    idade = 12
     #criando uma função / self é um parametro para diferenciar atributos de instancia, cada objeto criado dentro de uma classe, possui valores e atributos, o self garante que  esses valores sejam corretamente referenciados
    def saudacao(self):    
        print('olá mundo')


#output: 12
print(primeira_classe.idade)

#output: <function primeira_classe.saudacao at 0x000002063F928FE0> se retirar o parametro self e adicionar () apos saudacao no print, ira exibir 'ola mundo'
print(primeira_classe.saudacao)

#exibe a docstring na tela
print(primeira_classe.__doc__)