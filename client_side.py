import client_stub
function=input("Enter the function to be used ( Format:<func_name> <argument_1> <arguement_2>.......<arguement_n> ):\n")
def start():
    print("Starting the RPC")
try:
    string=eval(function+"()")
except:
    res=client_stub.middle(function)
    print("Result:",res)
