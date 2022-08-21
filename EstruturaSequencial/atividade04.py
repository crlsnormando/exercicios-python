#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

one_note = float(input("Entre com a primeira nota: "))
two_note = float(input("Entre com a segunda nota: "))
three_note = float(input("Entre com a terceira nota: "))
four_note = float(input("Entre com a quartaa nota: "))

total = one_note + two_note + three_note + four_note
average = total / 4
print(f" Media ds aluno: {average}")