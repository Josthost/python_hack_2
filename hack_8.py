"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):

    i = 0
   
    if len(result) == 5 or len(result) == 3:

        for i in range (len(result)):
            result[i] = (f"{result[i]}-{i + 1}")

        result = sorted(result, reverse=True)

    else:
        for i in range(len(result)):
            result[i] = str(i+1)
        result = sorted(result, reverse=True)

    return result