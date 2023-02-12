str1 = "[]{}()"
str2 = "[]{})"
str3 = "[{]}"

# symbols = {}
last_symbol = []
symbols_rules = {
    "[": {
        "condition": False,
        "symbol": "[",
        "partner": "]"
    },
    "{": {
        "condition": False,
        "symbol": "{",
        "partner": "}"
    },
    "(": {
        "condition": False,
        "symbol": "(",
        "partner": ")"
    },
    "]": {
        "condition": True,
        "symbol": "]",
        "partner": "["
    },
    "}": {
        "condition": True,
        "symbol": "}",
        "partner": "{"
    },
    ")": {
        "condition": True,
        "symbol": ")",
        "partner": "("
    }
}
for i in str3:
    # todo, если знаков не четное количество значит какой то не закрыт или не открыт
    if len(str3) % 2 != 0:
        print("Ошибка")
        break

    if not last_symbol:
        # todo проверка на первый символ, если он закрывающий то ошибка
        if symbols_rules.get(f"{i}")["condition"]:
            print(f"Ошибка: символ {i}")
            print("Подсказка: начинайте с {([")
        last_symbol.append(i)
    else:
        # todo проверка, если последний добавленный символ не открывает подаваемую скобку i, значит ошибка
        if last_symbol[-1]:
            # last_symbol.append(i)
            pass

# print(symbols)
#
# for i in symbols:
#     print(i)
