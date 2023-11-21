"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    remove = []

    
    clave = list(result.keys())

    for i in clave:
        if i == "bar" or i == "foo":
            result[i] = result[i].capitalize().replace("k", "")
            if i == "foo":
                result["Foo"] = result[i]
            remove.append(i)

    for i in remove:
        result.pop(i, None)

    return result

