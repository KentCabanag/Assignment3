def getName():
    _nm = input("Enter your name: ")
    return _nm

def getAge():
    _ag = input("Enter your age: ")
    return _ag

def getAddress():
    _add = input("Enter your address: ")
    return _add

def _format(_name, _age, _address):
    print(f"Hi, my name is {_name}. I am {_age} years old and I live in {_address}.")
    
name = getName()
age = getAge()
address = getAddress()
_format(name, age, address)
