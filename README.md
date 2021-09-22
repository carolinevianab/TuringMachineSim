# Simulador de Máquina de Turing
### Projeto feito para a matéria de Teoria da Computação do 6° Semestre de Ciência da Computação

### Por Caroline Viana

---

## Descrição
O projeto é a construção de um simulador de uma máquina de turing genérica, usando a linguagem Python.

O programa recebe um arquivo txt contento a descrição de uma máquina de turing, e consegue executar essa máquina, decidindo se palavras pertencem ou não a ela.

## Conteúdo e execução

O projeto, possui quatro arquivos necessários. É preciso baixar e manter ambos os arquivos na mesma pasta.
- `main.py`: arquivo principal do programa.
- `settings.py`: arquivo responsável pela configuração de cores.
- `TuringMachine.py`: arquivo contendo o código da máquina de turing.
- `content.txt`: descrição da máquina de turing

Para iniciar o programa, deve-se executar o arquivo main.py, tanto por IDE quanto por terminal, mas é importante haver espaço para que as informações possam ser impressas da forma desejada.

A impressão utiliza cores para imprimir as informações das palaavras no terminal. No entanto, essa cores podem não funcionar como esperado em alguns sistemas (como imprimir cores diferentes das esperadas.), pois ele imprime [códigos de escape ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code) para conseguir esse resultado.

