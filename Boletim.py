def calcular_media(notas, pesos=None):
    if pesos:       
        soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
        return soma_ponderada / sum(pesos)
    else:       
        return sum(notas) / len(notas)

def verificar_aprovacao(media):
    return media >= 7  

def main():
    nome = input("Digite o nome do aluno: ")
    serie = input("Digite a série do aluno: ")

    notas = []
    for i in range(4):  
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    fazer_ponderada = input("Gostaria de fazer média ponderada? (s/n): ").strip().lower()
    pesos = None

    if fazer_ponderada == 's':
        pesos = []
        for i in range(4):
            peso = float(input(f"Digite o peso da nota {i + 1}: "))
            pesos.append(peso)

    media = calcular_media(notas, pesos)

    aprovado = verificar_aprovacao(media)

    print(f"\nBoletim do Aluno: {nome}")
    print(f"Série: {serie}")
    print(f"Notas: {notas}")
    if pesos:
        print(f"Pesos: {pesos}")
    print(f"Média: {media:.2f}")
    print("Aprovado!" if aprovado else "Reprovado!")

if __name__ == "__main__":
    main()
