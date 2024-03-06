# Example of a call stack
def stackA():  # Defining Stack
    print('StackA() starts')
    stackB()
    stackD()
    print('stackA() returns')

def stackB():
    print('stackB() starts')
    stackC()
    print('stackB() returns')

def stackC():
    print('stackC() starts')
    print('stackC() returns')

def stackD():
    print('stackD() starts')
    print('stackD() returns')

stackA()
