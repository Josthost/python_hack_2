"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    if result == []:
        result.append("0")
    else:
        for i in range(len(result)):
            result[i] = str(i+1)
            if i % 2 == 1:
                result[i] = "-"

    return result