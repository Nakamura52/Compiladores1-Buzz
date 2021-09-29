from AnalisadorLéxico import Lexico
from Sintaxe import AnalisadorSintaxe
from Avaliador import AValiador

def main():
    filename = 'hello.buzz'
    file  = open(filename, 'r')
    lexico = Lexico(file)
    sintaxe = AnalisadorSintaxe(lexico.tokens)

    lexico.tokenizador()
    print("TOKENS")
    print(lexico.tokens, "\n")

    sintaxe.build_AST()
    print("AST:")
    print(sintaxe.AST, "\n")

    avaliador = AValiador(AnalisadorSintaxe.AST)
    print("OUTPUT:")
    avaliador.run(sintaxe.AST)

if __name__ == "__main__":
    main()