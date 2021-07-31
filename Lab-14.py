 
def heuristic_rules(word):
            
    if word.endswith('ie'):
       word = word.rstrip('ie')
       word = word+'y'+'ing'

    elif word.endswith('e'):
       if(word.endswith('ee') or word=='be'):
           word=word+'ing'
       else:
           word = word[:-1]
           word = word+'ing'
 
    elif word[-2] in 'aiou':
       word = word + word[-1] + 'ing'

    else:
       word = word +'ing'
 
    print(str(word))

word=str(input("enter a word")) 
heuristic_rules(word)
                           
    
