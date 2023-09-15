from enum import Enum

class genericKeyInputs(Enum):
    YES = "y"
    NO = "n" 

def genericTextInput():
    return input(">> ")

def binaryChoiceInput(question, aInput: str = genericKeyInputs.YES.value, bInput: str = genericKeyInputs.NO.value):
    print(question + f" ({aInput}/{bInput})")
    decision = input(">> ")
    if decision == aInput:
        return True
    elif decision == bInput:
        return False
    else:
        print(f"{decision} is not a valid key")
        print(f"The Valid Keys are [{aInput}/{bInput}]")
        return binaryChoiceInput(question,aInput,bInput)