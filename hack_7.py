"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    if result == [0]:
        result = [0]
    else:
        i = 0
        while i < len(result):
            result[i] = str(i + 1)
            if i % 2 == 1:
                result[i] = int(i + 1)
            i += 1
    return result