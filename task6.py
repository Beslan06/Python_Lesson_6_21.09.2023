# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.​

from Module.Queen import generate_queen_arrangement

NEAD_NUMBER_OF_POSITIONS = 4
CHESSBOARD_SIZE = 8  # Размер шахматной доски

arrangements = [generate_queen_arrangement(CHESSBOARD_SIZE) for _ in range(NEAD_NUMBER_OF_POSITIONS)]

for arrangement in arrangements:
    print(arrangement)

