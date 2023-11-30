# Função que lê dois números sem repetir a frase

def leitora_numeros() -> list:
    """Esta função faz a captura dos números a serem utilizados na calculadora e memoriza elas em lista"""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o {i+1}º número que deseja operar")))
        i+=1
    return numeros


def leitora_operacao() -> str:
    """Essa operação captura e memoriza a função da calculadora para executar sobre os dois números já memorizados"""
    operacao = input("""Digite a operação que deseja realizar.
Pressione + para adição;
- para subtração;
* para multiplicação;
/ para divisão""")
    return operacao


def leitora() -> list:
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]


def escritora(resultado: float) -> None:
    """Esta função coloca o resultado na tela."""
    print(f"O resultado da operação é igual a {resultado}.")