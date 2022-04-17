
class Games:
        def __init__(self ):
            pass
            
            
        def one_game(self, onegame):
            
            return f'I Have One Game Called "{onegame}"'
            
        def allgames(self,game):
            self.games = []
            print(e)
            print('I Have Many Games:')
            for i in e :
                 print(f'-{i} ')
                 
        def numgames(self, num):
            self.num = num
            return f'You Have {num} Games '

question = input('What is games do you play? ')
question2 = input('Do You Have Another Games ? y/n ').lower()
s = Games()
e = []
e.append(question)

if question in '0123456789' :
    print(s.numgames(question))
    
elif question2.lower() in 'no' and question2 != '0123456789':
    print(s.one_game(question))
    
elif question2.lower() in 'yes':
    while True :
        question3 = input('What is games do you play? ')
        e.append(question3)
        question4 = input('Do You Have Another Games ? y/n ').lower()
        if question4.lower() in 'no':
            print(s.allgames(e))
            break
            
        
        
        
        
    
    
    

        






