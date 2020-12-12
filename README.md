# bernsteinvazirani_qiskit

Implementação do problema de Bernstein-Vazirani no Qiskit

O problema de Bernstein-Vazirani é um dos primeiros algoritmos quânticos a serem propostos. É preliminar ao algoritmo de Shor, e de alguma forma expõe conceitos que serão úteis em algoritmos mais elaborados.

Imagine uma função que faz um XOR bit a bit entre duas strings.

Ex.

101 + 100 = 001
0011 + 1010 = 1001

Imagine que a função faz a soma entre uma string desconhecida e a string de entrada. A tarefa: descobrir a string desconhecida.

Exercício. Qual a string desconhecida para a função abaixo?

![](https://informacaoquantica.files.wordpress.com/2020/12/bern01.jpg)

Sugiro o leitor parar para resolver antes de prosseguir, porque a resposta está logo a seguir.

A forma de resolver classicamente é testando cada bit separadamente: (001, 010, 100), o que equivale a testar uma base da matriz identidade.

Se houver um flip do bit testado, a string é 1, se não, é 0.

![](https://informacaoquantica.files.wordpress.com/2020/12/bern02.jpg)

Portanto, classicamente temos que chamar a função N vezes, sendo N o número de bits da strings.

A proposta de Bernstein-Vazirani resolve o problema em uma única chamada ao oráculo (a caixa-preta que faz a computação)!

O algoritmo usa o truque do “coice de fase” (phase kickback).

Coloco todos os qubits de entrada em um estado de sobreposição, com portas Hadamard. Basicamente, a ideia aqui é testar todas as alternativas possíveis de um só vez.

A seguir, preparo o qubit do kickback com X (para transformar em 1), e um H.

![](https://informacaoquantica.files.wordpress.com/2020/12/alg01.jpg)

O oráculo deve ser preparado com a função que quero executar.

No exemplo, quero colocar a string ‘101’. Por isso, a caixa-preta tem um CX
(não controlado) nos qubits de controle 0 e 2, para o qubit controlado do
kickback.

![](https://informacaoquantica.files.wordpress.com/2020/12/alg02.jpg)

A seguir, uma série de Hadamards para tirar do estado de sobreposição, e a
medição do estado.

![](https://informacaoquantica.files.wordpress.com/2020/12/alg03.jpg)

Vide o circuito e o resultado: o circuito mediu ‘101’ nas 100 vezes em que foi
executado.

![](https://informacaoquantica.files.wordpress.com/2020/12/result.jpg)

Nesta simulação específica, eu sei exatamente o que está dentro da
caixa-preta, o que torna o problema apenas um exercício. Num caso geral, o
oráculo pode ser um problema que desconheço, aí sim tornando a função útil.

Mais um exemplo. Se eu quiser a string oculta ‘100’, coloco o CX no bit 0 apenas.
Note aqui uma grande ‘pegadinha’ do qiskit: a ordem de leitura dos qubits é ao
contrário. Imagine que o primeiro qubit, o dígito mais significativo é o de
baixo, por isso o resultado é ‘001’. A leitura é de baixo para cima, o reverso da lógica de entrada. Isso
causa muita confusão… em resumo, temos que reverter o resultado para ler corretamente.

![](https://informacaoquantica.files.wordpress.com/2020/12/result02.jpg)

Uma grande crítica ao Bernstein-Vazirani (e à computação quântica em geral): o
oráculo.

Por enquanto, o oráculo é algo que magicamente recebe os inputs e faz o processamento.

O oráculo deve ser algo muito especial. Deve ser capaz de receber todas as
entradas em superposição, fazer o processamento, e retornar a resposta num
formato processável em computação quântica.


Como construir esse oráculo? Se o oráculo processar cada alternativa da
superposição uma-a-uma, só estaremos jogando a sujeira para baixo do tapete:
fazemos só uma chamada à caixa-preta, mas dentro da caixa-preta tudo continua
igual. Para ter ganho real, na conta completa, o oráculo tem que ser considerado, a rigor.

Bom, se conseguirmos criar um oráculo que forneça uma aproximação da
resposta, a um custo computacional baixo, ainda saímos no lucro. Essa é uma
das primeiras respostas.

Uma segunda resposta envolve responder a pergunta por partes. Sendo o problema
completo muito difícil, vamos dividi-lo para facilitar a busca de soluções: o
algoritmo fora da caixa-preta apresenta os ganhos citados, e o problema da
caixa-preta fica aberto esperando respostas.

De qualquer forma, o problema citado não tem utilidade prática alguma, mas envolve conceitos
bastante importantes (caixa-preta, kickback) em discussões futuras.

Para ver a teoria do problema de Bernstein-Vazirani, recomendo o livro “Quantum Computer Science An Introduction”, David Mermin, que tem uma seção detalhando a matemática envolvida e uma discussão bem legal sobre o circuito quântico mencionado.

Código fonte no Github.


Veja também:

Forgotten Lore – Ideias técnicas com uma pitada de filosofia (ideiasesquecidas.com)
https://ideiasesquecidas.com/

Simulando o problema de Deutsch – Computação e Informação Quântica (wordpress.com)
https://informacaoquantica.wordpress.com/2020/04/23/simulando-o-problema-de-deutsch/

