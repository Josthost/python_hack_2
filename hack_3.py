"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    
    vocals = ["a", "e", "i", "o", "u","U"]
    r = ["@", "3", "¡", "0", "v","v"]

    result = result[0].upper() + result[1:-1] + result[-1].upper()

    for i, vocal in enumerate(vocals):
        result = result.replace(vocal, r[i])

    return result