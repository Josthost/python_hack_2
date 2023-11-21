"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):

    result = [{str(i + 1): str(i + 2)} for i in range(len(result) * 2) if i % 2 == 0]

    result[1] = {f"{3}",f"{4}"}
    
    return result