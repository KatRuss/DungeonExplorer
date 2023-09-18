from enum import Enum

class genericKeyInputs(Enum):
    YES = "y"
    NO = "n" 

def genericTextInput():
    return input(">> ")

def binaryChoiceInput(question:str, aInput: str = genericKeyInputs.YES.value, bInput: str = genericKeyInputs.NO.value):
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
    
def listChoiceInput(question:str, li:list):
        print(question)
        for x in range(0,len(li)):
             print(f"{x+1}: {li[x]}")
        choice = int(genericTextInput())
        if choice >= 1 and choice <= len(li):
             return li[choice-1]
        else:
            print(f"{choice} is not a valid key")
            return listChoiceInput(question,li)