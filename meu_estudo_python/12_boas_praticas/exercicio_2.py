# EXERCÍCIO: Calculadora de IMC
# Objetivo: Aplicar type hints e funções organizadas

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o Índice de Massa Corporal"""
    # IMC = peso / altura²
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    """Classifica o resultado do IMC"""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def exibir_resultado(nome: str, peso: float, altura: float) -> None:
    """Mostra o resultado completo"""
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"\n{'='*30}")
    print(f"Nome: {nome}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.1f}")
    print(f"Classificação: {classificacao}")
    print(f"{'='*30}")

def main() -> None:
    """Função principal"""
    print("═══ Calculadora de IMC ═══\n")
    
    while True:
        try:
            nome = input("Nome: ")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))
            
            # Validação básica
            if peso <= 0 or altura <= 0:
                print("✗ Valores devem ser maiores que zero!")
                continue
            
            exibir_resultado(nome, peso, altura)
            
            continuar = input("\nCalcular para outra pessoa? (s/n): ").strip().lower()
            if continuar != "s":
                print("Encerrando. Até mais!")
                break
        except ValueError:
            print("✗ Digite apenas números!")

if __name__ == "__main__":
    main()

# COMO FUNCIONA:
# 1. Pede nome, peso e altura
# 2. Calcula: IMC = peso / altura²
# 3. Classifica: <18.5 = abaixo, 18.5-25 = normal, etc
# 4. Mostra o resultado formatado
