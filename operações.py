def soma(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return round(n1/n2,2)
def multi(n1,n2):
    return n1*n2
def pot(n1,n2):
    return n1**n2
def operaçõesST(n1=1,n2=2,operação="+"):
    match operação:
        case "+":
            return soma(n1,n2)
        case "-":
            return sub(n1,n2)
        case "x":
            return multi(n1,n2)
        case "/":
            return div(n1,n2)
        case _:
            return pot(n1,n2)
if __name__=="__main__":
    operaçõesST()
        
