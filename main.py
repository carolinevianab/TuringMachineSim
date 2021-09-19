from TuringMachine import TuringMachine
from settings import bcolors as bc

# Imprimindo o header
print(f"""{bc.MAGENTA}********************************************************************** 
Welcome to the Turing Machine{bc.ENDC}

To run the machine on the test words, use the function {bc.UNDERLINE}runMachineOnTests{bc.ENDC}.
If you like to use the machine with your own input, use the function {bc.UNDERLINE}run{bc.ENDC} with your word as a parameter.
{bc.CYAN}
Made by Caroline Viana
as a Computer Theory Project
{bc.ENDC}
{bc.MAGENTA}********************************************************************** {bc.ENDC}
""")

# ----- Testando a máquina ----- #

# Rodando a máquina nas palavras de teste
mt = TuringMachine("content.txt")
mt.runMachineOnTests()

# Rodando a máquina numa palavra que eu estou colocando
mt.run("aabaa")
mt.run("-")
mt.run("oba")