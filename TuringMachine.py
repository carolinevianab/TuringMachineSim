from settings import bcolors as bc

class TuringMachine:
  file = ""         # Arquivo de entrada
  tape = []         # Fita da máquina

  # O arquivo de entrada será dividido em
  alphabet = ""     # Alfabeto
  transitions = []  # Array de transições
  q0 = ""           # Estado inicial
  qAccept = ""      # Estado de aceitação
  testWords = []    # Array de palavras de teste

  #  __init__: Recebe como parâmetro o nome do arquivo de entrada
  # Abre o arquivo de entrada e chama a função de separação das informações
  def __init__(self, fileName):
    self.file = open(fileName, "r")
    self.separate()

# ------------------------------------------------------------------------ #

  # separate
  # Separa todas as informações do arquivo em suas respectivas variáveis, de forma a facilitar o uso pela máquina
  def separate(self):
    lines = self.file.readlines()
    
    # Grava alfabeto da fita
    self.alphabet = self.removeSlashN(lines[0])

    # Mensagem de erro caso o alfabeto possua mais de 30 símbolos.
    if len(self.alphabet) > 30:
      print("Error: Number of symbols on alphabet exceeded the maximum value of 30.")
      return

    # Mensagem de erro caso a máquina possua mais de 50 estados.
    if int(lines[1]) > 50:
      print("Error: Number of states exceeded the maximum value of 50.")
      return

    # Grava o último estado disponível, que será o estado de aceitação
    self.qAccept = self.removeSlashN(lines[1])

    # Assume-se que o estado inicial seja sempre q1
    self.q0 = "1"

    # Percorre todas as transições (baseado na quantidade de transições) salvando cada uma como array e sendo adicionada a lsita de transições
    transitionQtt = int(lines[2])
    counter = 3
    while True:
      transition = lines[counter]
      transitionArray = transition.split()
      self.transitions.append(transitionArray)
      counter += 1
      if counter - 3 >= transitionQtt:
        break

    # Mensagem de erro caso a quantidade de palavras para teste seja maior que 100
    wordQtt = int(lines[counter])
    if wordQtt > 100:
      print("Error: Number of words exceeded the maximum value of 100.")
      return

    # Percorre todas as palavras de teste (baseado na quantidade de palavras) salvando-as na lista de palavras de teste
    counter+= 1
    while True:
      word = lines[counter]
      self.testWords.append(self.removeSlashN(word))
      counter += 1
      if counter >= len(lines):
        break
    
    self.file.close()

# ------------------------------------------------------------------------ #
    
  # removeSlashN: Recebe como parâmetro uma palavra
  # Remove o divisor de linha "\n" das strings
  def removeSlashN(self, word):
    return str(word.replace("\n", ""))

# ------------------------------------------------------------------------ #

  # run: Recebe uma palavra como parâmetro
  # Executa a Máquina de Turing com as instruções passadas sob a palavra recebida
  def run(self, word):
    print("----------")
    self.tape.clear()

    state = self.q0
    readerPosition = 1

    # Gravamos a palavra na fita com um espaço em branco no começo e no fim da fita, para caso sejam necessários
    self.tape.append("-")
    for char in word:
      self.tape.append(char)
    self.tape.append("-")

    while True:
      # Testa se estamos no estado de aceitação
      if state == self.qAccept:
        print(word, f"{bc.GREEN}OK{bc.ENDC}")
        return

      # Mensagem de erro caso o caractere da fita não esteja presente no alfabeto de entrada (e não seja um espaço em branco)
      if self.tape[readerPosition] not in self.alphabet and self.tape[readerPosition] not in "-":
        print(f"Error in word {bc.YELLOW}\"{word}\"{bc.ENDC}: Character not present in tape alphabet.")
        print(word, f"{bc.RED}NOT OK{bc.ENDC}")
        return

      # Percorre a lista de transições até encontrar a correta, e executa as instruções daquela transição
      for transition in self.transitions:
        if transition[0] == state and transition[1] == self.tape[readerPosition]:
          self.tape[readerPosition] = transition[2]
          state = transition[4]
          if transition[3] == "D":
            readerPosition += 1
          else:
            readerPosition -= 1
          break

        # Caso tenhamos chegado a última transição disponível na lista, e nenhuma delas foi a transição correta, significa que não há uma transição daquele estado/daquele caractere
        # Ou seja, a fita é rejeitada
        if transition == self.transitions[-1]:
          print(word, f"{bc.RED}NOT OK{bc.ENDC}")
          return
 
# ------------------------------------------------------------------------ #

  # runMachineOnTests
  # Executa a Máquina de Turing com as instruções passadas sob as palavras de teste
  def runMachineOnTests(self):
    for word in self.testWords:
      self.run(word)

## Arquivo TXT -> Estrutura ##
# Linha 1: alfabeto de entrada + alfabeto da fita, <= 30
# Linha 2: qtd de estados, ultimo sempre é aceitação, <= 50
# Linha 3: qtd n de transições
# Linha 4 a Linha n: transições
# Linha n+1: qtd p de palavras pra teste
# Linha n+2 a Linha n+2+p: palavras de teste, p<= 100