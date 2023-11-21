"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    
    vocals = ["a", "e", "i", "o", "u"]

    for vocal in vocals:
        result = result.replace(vocal, "")

    return result