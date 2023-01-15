
def Seperate_Symbol_from_Name(name):
    symbol=''
    while name[0].isupper() and name[1].isupper():
            symbol+=name[0]
            name=name[1:]
    return    [symbol,name] 

def Remove_Non_Capitals(string):
    while not string[0].isupper():
        string=string[1:] 
    return string 


def split_string_by_two(s):
    s=s[int(len(s)/2):]
    return(s)     

