'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Função para converter temperatura
def converter_temperatura(valor, origem, destino):
    if origem == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        elif destino == "K":
            return valor + 273.15
    elif origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return valor  # se origem e destino forem iguais

# Entrada do usuário
valor = float(input("Digite o valor da temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Validação simples
if origem not in ["C", "F", "K"] or destino not in ["C", "F", "K"]:
    print("Unidades inválidas. Use apenas C, F ou K.")
else:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"{valor:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
