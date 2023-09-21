from date_validator import is_valid_date

if __name__ == "__main__":
    date = "21.09.2023"  # Это високосный год, 29 февраля существует
    if is_valid_date(date):
        print(f"{date} существующая дата.")
    else:
        print(f"{date} некорректная дата.")