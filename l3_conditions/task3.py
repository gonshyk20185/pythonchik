# Do not remove this import
from enum import Enum


# Do not change this class
class Keyword(Enum):
    IF = "if"
    WHILE = "while"
    FOR = "for"
    CLASS = "Class"
    IDENTIFIER = None


# Finish the function body to make the script work without errors
def word2token(word: str) -> Keyword:
    mapping = {
        "if": Keyword.IF,
        "while": Keyword.WHILE,
        "for": Keyword.FOR,
        "class": Keyword.CLASS
    }
    return mapping.get(word, Keyword.IDENTIFIER)


# Do not change the below's code
if __name__ == "__main__":
    assert word2token("if") == Keyword.IF
    assert word2token("while") == Keyword.WHILE
    assert word2token("for") == Keyword.FOR
    assert word2token("class") == Keyword.CLASS
    assert word2token("anything") == Keyword.IDENTIFIER
    assert word2token("something") == Keyword.IDENTIFIER
