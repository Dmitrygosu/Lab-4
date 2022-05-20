""" 30.	Формируется матрица F следующим образом: если в В количество простых чисел в нечетных столбцах в области 2 больше, чем произведение чисел по периметру области 3,
то поменять в В симметрично области 1 и 3 местами, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A T)*(F+А)-K* F T .
 Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import time


def is_simple_number(x):
    divider = 2
    if x < 0 or x == 0:
        return False
    while divider < (x**0.5):
        if x % divider == 0:
            return False
        divider += 1
    return True
def print_matrix(Matrix, matrix_name, timetime):
        print ( f"матрица {matrix_name} промежуточное время = {round(timetime, 2)} seconds")
        for i in Matrix:            # Делаем перебор всех строк матрицы
            for j in i:     # Перебираем все элементы в строке
                print("%5d" % j, end=" ")
            print()
print("\n")
try:
    matrix_size = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while matrix_size < 6 or matrix_size > 100:
        matrix_size = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, AT, FT, FA = [], [], [], [], []      # Задаем матрицы
    for i in range(matrix_size):
        A.append([0] * matrix_size)
        F.append([0] * matrix_size)
        AT.append([0] * matrix_size)
        FA.append([0] * matrix_size)
        FT.append([0] * matrix_size)
    time_next = time.time()
    print_matrix(F, "F", time_next-start)

    for i in range(matrix_size):
        for j in range(matrix_size):
            A[i][j] = random.randint(-10, 10)
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next-time_prev)

    for i in range(matrix_size):
        for j in range(matrix_size):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next-time_prev)

    B = []  # Задаем матрицу B
    submatrix_size = matrix_size // 2
    for i in range(submatrix_size):
        B.append([0] * submatrix_size)
    for i in range(submatrix_size):
        for j in range(submatrix_size):
            B[i][j] = F[i][submatrix_size + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(B, "B", time_next - time_prev)

    kol_vo = 0
    proizv = 1
    index = 0

    # Произведение элементов по периметру
    for x in range(submatrix_size-1, submatrix_size//2-1, -1):
        for y in range(submatrix_size-1, submatrix_size//2, -1):
            proizv *= B[x][-1-index]
            index += 1
            break


    if submatrix_size % 2 == 1:
        index = 0
        for i in range(submatrix_size//2+1, submatrix_size, 1):  # Обрабатываем подматрицу E
            for j in range(submatrix_size//2-1, 0-1, -1):
                proizv *= B[i][j-index]
                index += 1
                break

    else:
        index = 0
        for i in range(submatrix_size//2, submatrix_size, 1):
            for j in range(submatrix_size//2-1, 0, -1):
                proizv *= B[i][j-index]
                index += 1
                break


    print("#" * 100)
    for j in range(1, submatrix_size - 1):
        i = submatrix_size-1
        proizv *= B[i][j]


    for i in range(submatrix_size, matrix_size-1):
        for j in range(i + 1, submatrix_size, 1): # Обработка подматрицы B
            if is_simple_number(B[i][j]) == True and j % 2 == 1 and j > submatrix_size - 1 - i:
                kol_vo += 1

    if kol_vo > proizv:
        print("Случай 1")
        for i in range((submatrix_size // 2)-1):  # Меняем 1 и 3 области симметрично
            for j in range(1, submatrix_size-1):
                b1 = j > i
                b2 = j < submatrix_size - 1 - i
                if b1 and b2:
                    B[i][j], B[submatrix_size - 1 - i][j] = B[submatrix_size - 1 - i][j], B[i][j]

    else:
        print("Случай 2")
        for j in range(0, matrix_size // 2 + matrix_size % 2 - 1, 1): # Меняем подматрицы Е и С местами несимметрично
            for i in range(matrix_size // 2):
                F[i][matrix_size // 2 + matrix_size % 2 + j], F[matrix_size // 2 + matrix_size % 2 + i][matrix_size // 2 + matrix_size % 2 + j] = F[matrix_size // 2 + matrix_size % 2 + i][matrix_size // 2 + matrix_size % 2 + j], F[i][matrix_size // 2 + matrix_size % 2 + j]
    print_matrix(B, "B", time_next - time_prev)
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    for i in range(matrix_size):  # A^T
        for j in range(i, matrix_size, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(matrix_size):  # F^T
        for j in range(i, matrix_size, 1):
            FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T", time_next - time_prev)

    for i in range(matrix_size):      # K*A^T
        for j in range(matrix_size):
            AT[i][j] = K*AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K*A^T", time_next-time_prev)

    for i in range(matrix_size):
        for j in range(matrix_size): # F+A
            FA[i][j] = F[i][j] + A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "FA", time_next - time_prev)

    for i in range(matrix_size):      # K*A^T
        for j in range(matrix_size):
            FT[i][j] = K*FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "K*FT", time_next-time_prev)

    for i in range(matrix_size):
        for j in range(matrix_size):
            FA[i][j] = FA[i][j]*AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "FA", time_next - time_prev)

    for i in range(matrix_size):
        for j in range(matrix_size):
            FA[i][j] = FA[i][j] - FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "FA", time_next - time_prev)

    print(f"Program time: {round(time.time()-start,3)} seconds.")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.")
