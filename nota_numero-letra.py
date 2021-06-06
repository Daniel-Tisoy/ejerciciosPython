# entrada
nota = int(input('Nota númerica'))

if (nota > 100) or (nota < 0):
    print('nota por fuera del rango (0-100)')
# proceso
else:
    if nota >= 90:
        print('Su nota es A')
    elif 80 <= nota:
        print('Su nota es B')
    elif 70 <= nota:
        print('Su nota es C')
    elif 60 <= nota:
        print('Su nota es D')
    else:
        print('Su nota es F')

# solucion 2
if nota >= 90:
    nota = 'A'
else:
    if nota >= 80:
        nota = 'B'
    else:
        if nota >= 70:
            nota = 'C'
        else:
            if nota >= 60:
                nota = 'D'
            else:
                nota = 'F'
print(f'\n su nota en letra es {nota}')
