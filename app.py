#def greet(name):
 #   print("hello "+ name+ " . How are you?")
#greet("dhairya") 

def countWords():
    f = input(' Enter The File Name ')  
    nw = 0
    file = open(f,'r')
    for l in file:
        words = l.split()
        nw = nw+len(words)  
    print('number of words :-')
    print(nw)


countWords()    
    


    
