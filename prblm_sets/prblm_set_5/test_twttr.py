#testing shorten() fn
from twttr import shorten
#diff categories to test diff types
def test_small_vwl():#for small vowels
    assert shorten("moffasir")=="mffsr"
    assert shorten("980")=="980"

def test_capital_vwl(): #for capital vowls
    assert shorten("MOFFASIR")=="MFFSR"
    assert shorten("?")=="?"

def test_mixed_vwl():#for mixed sized vowls
    assert shorten("mOffaSIr")=="mffSr"

