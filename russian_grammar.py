
grammar = """
    start: (WS* expr WS*)*

    expr: "ЧЛЕН " varname " " value -> setdick
        | "ВЗЯТЬ " value -> grab
        | "ОТПУСТИТЬ " varname -> release
        | "БОЛЬШОЙ ЧЛЕН " value -> longdick
        | "МАЛЕНЬКИЙ ЧЛЕН " value -> smalldick
        | "ОГРОМНЫЙ ЧЛЕН " value -> hugedick
        | "КРОШЕЧНЫЙ ЧЛЕН " value -> tinydick
        | "ПИСАТЬ" -> pee
        | "ВИСАТЬ" -> wee
        | startif condition cockblock endif -> conditional
        | startwhile condition cockblock endwhile -> while

    cockblock: (WS* expr WS*)*

    startif: "ЧЕКАЙ! "
    condition: value " БОЛЬШЕ " value "!" -> bigger
             | value " МЕНЬШЕ " value "!" -> smaller
             | value " РАВЕН " value "!" -> equal
    endif: "ШУТКИ ПРО ПИСЬКИ? ТЕБЕ СКОЛЬКО ЛЕТ"

    startwhile: "ХУЯРИТЬ, ЕСЛИ "
    endwhile: "ТАК, ЗАКОНЧИЛИ ХУЯРИТЬ"

    value: dick | varname

    dick: "8" dickmid* "D"
    dickmid: "="
    varname: CNAME

    // imports
    %import .common_russian.CNAME
    %import common.WS

    // ignore indentation
    %ignore /\\t/
    %ignore "    "
"""

required_words_in_varnames =  ["Хуй", "Хер", "Член", "Пенис", "Болт", "Писька", "Шланг", "Писюн", "Аппарат", "Хозяйство", "Шишка", "Достоинство", "Дрын"]
