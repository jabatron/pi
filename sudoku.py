def leer_fila(i):
    while True:
        fila=input(f'Introuduce la fila {i}: ')
        if len(fila) != 9 or not fila.isdigit():
            continue
        else:
            break

    return [int(i) for i in fila]


def print_sudoku(s):
    for i in range(9):
        print (s[i])

def comprobar_fila(sudoku, fila):
    fila = sudoku[fila]
    for i in range(1,10):
        if fila.count(i)!=1:
            print (fila, fila.count(i), i)
            return False

    return True

def comprobar_columna(sudoku, columna):
    c=[]
    for i in range(9):
        c.append(sudoku[i][columna])

    for i in range(1,10):
        if c.count(i)!=1:
            return False

    return True

def comprobar_filas(sudoku):
    for i in range (9):
        r = comprobar_fila(sudoku, i)
        if not r:
            return False

    return True

def comprobar_columnas(sudoku):
    for i in range (9):
        r = comprobar_columna(sudoku, i)
        if not r:
            return False

    return True

def sacar_3x3(sudoku, t):
    l=[]
    ii = (t // 3) * 3
    jj = (t % 3) * 3
    
    for i in range(3):
        for j in range (3):
            l.append(sudoku[i+ii][j+jj])
    return l

def comprobar_3x3(mini):
    for i in range(1,10):
        if mini.count(i)!=1:
            return False

    return True

def comprobar_minis(sudoku):
    for i in range(9):
        r = comprobar_3x3(sacar_3x3(sudoku, i))
        if not r:
            return False
    return True


if __name__ == "__main__":
    sudoku = []
    for i in range (1,10):
        sudoku.append(leer_fila(i))

    print('\n\n\n')
    print_sudoku(sudoku)

    print (comprobar_columnas(sudoku) and comprobar_filas(sudoku) and comprobar_minis(sudoku))

    
    