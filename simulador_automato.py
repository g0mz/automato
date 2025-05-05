import json
import sys
import time

def carregar_automato(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)

def carregar_entradas(caminho):
    with open(caminho, 'r') as f:
        return [linha.strip().split(';') for linha in f if linha.strip()]

def salvar_saida(caminho, resultados):
    with open(caminho, 'w') as f:
        for linha in resultados:
            f.write(';'.join(linha) + '\n')

def simular_afd(automato, palavra):
    estado_atual = automato['initial']
    transicoes = automato['transitions']
    
    for simbolo in palavra:
        proximo = None
        for trans in transicoes:
            if trans['from'] == estado_atual and trans['read'] == simbolo:
                proximo = trans['to']
                break
        if proximo is None:
            return False
        estado_atual = proximo

    return estado_atual in automato['final']

def main():
    if len(sys.argv) != 3:
        print("Uso: python simulador_automato.py <automato.aut> <entrada.in>")
        sys.exit(1)

    caminho_automato = sys.argv[1]
    caminho_entrada = sys.argv[2]
    caminho_saida = 'resultado_obtido.out'

    automato = carregar_automato(caminho_automato)
    entradas = carregar_entradas(caminho_entrada)

    resultados = []

    for palavra, esperado in entradas:
        inicio = time.perf_counter()
        resultado = simular_afd(automato, palavra)
        fim = time.perf_counter()

        obtido_int = 1 if resultado else 0
        tempo = fim - inicio

        tempo_formatado = f"{tempo:.6f}"

        resultados.append([palavra, esperado, str(obtido_int), tempo_formatado])

    salvar_saida(caminho_saida, resultados)
    print(f"Simulação concluída. Resultados salvos em '{caminho_saida}'.")

if __name__ == "__main__":
    main()

