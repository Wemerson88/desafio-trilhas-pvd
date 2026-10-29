compras = []

print("=== Sistema de Ponto de Vendas === (digite para encerrar)")

while True:
    valor = float(input("\nValor da compra (R$): "))

    if valor < 0:
        print("O valor não pode ser negativo. Tente novamente.")
        continue

    if valor == 0:
        break

    while True:
        idade = int(input("Idade do cliente: "))
        if idade < 0:
            print("A idade não pode ser negativa. Tente novamente.")
            continue
        break

    final = valor

    if idade >= 65:
        final = round(final * 0.80, 2)

    if final > 100:
        final = round(final * 0.90, 2)

    compras.append((valor, final))
    print(f"Valor final: R$ {final:.2f}")

total_bruto = 0
total_final = 0

for compra in compras:
    total_bruto += compra[0]
    total_final += compra[1]

total_descontos = total_bruto - total_final

print("\n===== VENDAS DO DIA =====")
print(f"Compras registradas: {len(compras)}")
print(f"Total bruto:         R$ {total_bruto:.2f}")
print(f"Total de descontos:  R$ {total_descontos:.2f}")
print(f"Total final:         R$ {total_final:.2f}")