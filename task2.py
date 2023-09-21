# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def generate_bonus_dict(names, rates, bonuses):
    bonus_dict = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        bonus_percentage = float(bonus.rstrip('%'))
        bonus_amount = round(rate * bonus_percentage / 100, 2)
        bonus_dict[name] = bonus_amount
    return bonus_dict

# Пример использования функции-генератора
names = ["София", "Малик", "Адам"]
rates = [1000, 1500, 800]
bonuses = ["10.25%", "8.5%", "12%"]

bonus_dict = generate_bonus_dict(names, rates, bonuses)
print(bonus_dict)
