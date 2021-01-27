# Trabalho 2 - Teoria da Informação
## Ana Carolina Silva
### up202004100

## Dependências
De modo a utilizar o módulo é necessário instalar a biblioteca *bitstring* e *numpy*.

## Como utilizar o módulo

No início do seu código python faça o *import* das funções que pretende utilizar da seguinte forma
```py
from ldpc.py import encode, decode
```

### Como gerar um código de bloco?
Comece por dar import da função *generate_code*.

Esta função recebe 3 inputs
- *k*: tamanho da mensagem a codificar
- *m*: número de vezes que cada bit da mensagem será utilizado
- *v*: número de bits necessários para gerar um bit de paridade

A função retorna uma lista de tamanho *m(k/v)* com listas de tamanho *v*.

Exemplo:
```py
k = 9
m = 2
v = 2
P = generate_code(k, m, v)
```

### Como codificar uma mensagem?
Comece por dar import da função *encode*.

A função necessita de 3 argumentos
- *k* : tamanho da mensagem a codificar
- *P* : código de blocos gerado (ver função *generate_code*)
- *w* : mensagem a codificar

A função retorna um *BitArray* com a mensagem *w*, à qual são concatenados os bits de paridade.

Exemplo:
```py
k = 32
m = 8
v = 4
w = BitArray('0b01001000010001110111100010010101')
P = generate_code(k, m, v)
x = encode(k, P, w)
```

### Como descodificar um código?
Comece por dar import da função *decode*.

A função necessita de 4 argumentos
- *k* : tamanho da mensagem a codificar
- *P* : código de blocos gerado (ver função *generate_code*)
- *y* : código recebido do canal de rasura
- *q* : erros detetados no código *y*

A função retorna um *BitArray* com a mensagem *w* descodificada ou *None* caso não seja possível a sua descodificação.

Exemplo:
```py
k = 8
m = 2
v = 2
P = generate_code(k, m, v)
y = BitArray('0b0001000101101100')
q = BitArray('0b1110101000000010')
x = decode(k, P, y, q)
```
