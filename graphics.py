import time
import streamlit as st

def hanged(man):
    graphic = [
        '''
        Try your luck! and guess the word.
              +--------+
              |        
              |        
              |        
              |        
              |        
           ==============
        ''',
        '''
        Ga
              +--------+
              |        |
              |        O
              |        
              |        
              |        
           ==============
        ''',
        '''
        Gam
              +--------+
              |        |
              |        O
              |        |
              |        
              |        
           ==============
        ''',
        '''
        Game
              +--------+
              |        |
              |        O
              |       -|
              |        
              |        
           ==============
        ''',
        '''
        Game O
              +--------+
              |        |
              |        O
              |       -|-
              |        
              |        
           ==============
        ''',
        '''
        Game Ov
              +--------+
              |        |
              |        O
              |       -|-
              |       / 
              |        
           ==============
        ''',
        '''
        Game Over! 
              +--------+
              |        |
              |        O
              |       -|-
              |       / \\
              |        
           ==============
        '''
    ]
    return graphic[min(man, 6)]  

def display_hangmen(state, st):
    st.code(hanged(state.letters_wrong), language='')

def celebration_animations():
    CELEBRATION_FRAMES = [
        '''
        Celebration! 
                                    
                      O
                     /|\\
                     / \\
                      
           
        '''
        ,
        '''
        Celebration! 
                                    
                     \O/
                      |
                     / \\
            
        '''
        ,
        '''
        Celebration! 
              
                      O
                     /|/
                     / \\
             
        '''
        ,
        '''
        Celebration! 
                               
                      O
                     \|\\
                     / \\
                     
           
        '''
        ,
        '''
        Celebration! 
              
                     \O/
                      |
                     / \\
              
        '''
    ]


    hangman_display = st.empty()
    for _ in range(8):
        for frame in CELEBRATION_FRAMES:
            hangman_display.write(f"```{frame}```")
            time.sleep(0.3)

