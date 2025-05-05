# Simulador de Autômatos Finitos

## Descrição

Este projeto implementa um simulador de autômatos finitos em Python. A ferramenta lê a definição de um autômato a partir de um arquivo JSON e testa uma série de palavras a partir de um arquivo CSV. O simulador verifica se cada palavra é aceita ou rejeitada pelo autômato e gera um relatório com os resultados.

## Funcionamento

1. **Arquivo do autômato (JSON)**: Define o autômato com o estado inicial, os estados finais e as transições entre os estados para cada símbolo.
2. **Arquivo de entradas (CSV)**: Contém as palavras a serem testadas, juntamente com o resultado esperado (1 para aceito, 0 para rejeitado).
3. **Código**: O programa carrega o arquivo JSON e define o autômato, depois carrega os arquivos de entrada, percorre cada palavra símbolo por símbolo seguindo as transições do autômato e verifica se o estado final ao fim da palavra é um estado de aceitação.
4. **Arquivo de saída**: O simulador gera um arquivo com o resultado de cada teste, incluindo a palavra, o resultado esperado, o resultado obtido e o tempo de execução.

## Exemplo de Uso

### Exemplo de Arquivo JSON (automato.json)

```bash
{
  "initial": "0",
  "final": ["2"],
  "transitions": [
    { "from": "0", "to": "0", "read": "a" },
    { "from": "2", "to": "2", "read": "a" },
    { "from": "1", "to": "1", "read": "b" },
    { "from": "1", "to": "2", "read": "a" },
    { "from": "0", "to": "1", "read": "b" }
  ]
}
```

### Exemplo de Arquivo CSV (entradas.csv)

```bash
ba;1
aaaabbbbbaaaaa;1
abababab;0
bbbbbbbb;0
aaaaaaaaaaaa;0
aaaaabaaaaa;1
```

### Execução

 Execute o simulador com os arquivos como parâmetros:

```bash
$ python simulador_automato.py automato.json entradas.csv
```
### Exempo de Saída

```bash
ba;1;0;0.000003
aaaabbbbbaaaaa;1;0;0.000002
abababab;0;0;0.000001
bbbbbbbb;0;0;0.000000
aaaaaaaaaaaa;0;0;0.000001
aaaaabaaaaa;1;0;0.000001
```
Cada espaço entre ";" representa:

1. a palavra testada,

2. o resultado esperado,

3. o resultado obtido pelo simulador,

4. o tempo de processamento.


