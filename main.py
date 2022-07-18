import pytest

def toUpperCase1(word):
    return word.upper()

def toUpperCase2(word):
    ans = ""
    for character in word:
        ans = ans + character.upper() + "5"
    return ans

def test_method():
    word = "chANge To UppercaSE"
    wordInUpperCaseFromFirstMethod = toUpperCase1(word)
    print(wordInUpperCaseFromFirstMethod)
    wordInUpperCaseFromSecondMethod = toUpperCase2(word)
    print(wordInUpperCaseFromSecondMethod)
    assert wordInUpperCaseFromFirstMethod == wordInUpperCaseFromSecondMethod, "there is a bug in your method"


