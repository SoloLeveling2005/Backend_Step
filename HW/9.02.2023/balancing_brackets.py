str1 = "( ( ( )  ) )"
str2 = "[]{})"
str3 = "[{]}"


# symbols = {}


def balanced(data):
    symbols = []
    error = False
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
    index = 0
    data = data.replace(" ", "")

    for j, i in enumerate(data):
        # todo, если знаков не четное количество значит какой то не закрыт или не открыт
        if len(data) % 2 != 0:
            print("Ошибка, не все скобки закрыты или открыты")
            error = True
            break

        if not symbols:
            # todo проверка на первый символ, если он закрывающий то ошибка
            if symbols_rules.get(f"{i}")["condition"]:
                print(f"Ошибка: символ {i}")
                print("Подсказка: начинайте с {([")
                print(f"Ошибка в символе под индексом {j}")
            symbols.append(i)
        else:
            # todo symbol - данные поданного знака
            present_symbol_info = symbols_rules.get(f"{i}")
            past_symbol = symbols[-1]

            # todo (present_symbol) проверяем закрывающий знак или открывающий
            if present_symbol_info['condition'] is False:
                # todo знак открывающий, значит
                # todo нам НЕ принципиально какой был знак до этого
                symbols.append(i)
            else:
                # todo знак закрывающий, значит
                # todo если прошлый знак НЕ соответствует партнеру present_symbol то мы выдаем ошибку
                if past_symbol != present_symbol_info['partner']:
                    print("Скобка не правильно закрыта")
                    print(f"Ошибка в символе под индексом {j}")
                    error = True
                    break
                # todo если прошлый знак соответствует партнеру present_symbol то мы удаляем прошлый знак
                if past_symbol == present_symbol_info['partner']:
                    symbols = symbols[:-1]

    if not error:
        print("Ошибок не обнаружено")


balanced(str1)
