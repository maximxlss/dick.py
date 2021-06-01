
grammar = """
    start: (WS* expr WS*)*

    expr: "DICK " varname " " value -> setdick
        | "GRAB " value -> grab
        | "RELEASE " varname -> release
        | "LONGDICK " value -> longdick
        | "SMALLDICK " value -> smalldick
        | "HUGEDICK " value -> hugedick
        | "TINYDICK " value -> tinydick
        | "PEE" -> pee
        | "WEE" -> wee
        | startif condition cockblock endif -> conditional
        | startwhile condition cockblock endwhile -> while

    cockblock: (WS* expr WS*)*

    startif: "LOOK! "
    condition: value " IS BIGGER THAN " value "!" -> bigger
             | value " IS SMALLER THAN " value "!" -> smaller
             | value " IS JUST LIKE " value "!" -> equal
    endif: "DICK JOKES ARE IMMATURE, SERIOUSLY"

    startwhile: "COCK GO FAST IF"
    endwhile: "ALRIGHT, STOP COCKING AROUND"

    value: dick | varname

    dick: "8" dickmid* "D"
    dickmid: "="
    varname: CNAME

    // imports
    %import common.CNAME
    %import common.WS

    // ignore indentation
    %ignore /\\t/
    %ignore "    "
"""

required_words_in_varnames =  ["Johnson", "Dick", "Cock", "Schlong", "Penis", "Dong"]
