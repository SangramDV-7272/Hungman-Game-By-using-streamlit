import streamlit as st
from hidden_pattern import initialize_game, display_game_info, offer_hint
from user_input import handle_guess, display_guessed_letters
from check_input import check_game_over, reset_game
from graphics import display_hangmen, celebration_animations



def main():
    st.set_page_config(page_title="Hangman Game", layout="wide")
    st.title("Hangman Game")
    
    initialize_game(st.session_state)
    col1, col2 = st.columns(2)
    
    with col1:
        display_game_info(st.session_state, st)
        offer_hint(st.session_state, st)
        
        if not st.session_state.game_over:
            if "letter" not in st.session_state:
                st.session_state.letter = ""
            
            def clear():
                st.session_state.letter = st.session_state.widget
                st.session_state.widget = ""
                return st.session_state.letter
            
            st.text_input("Guess a letter:", max_chars=1, key="widget", placeholder="Write a letter...", on_change=clear).lower()
            letter = st.session_state.letter
            
            display_guessed_letters(st.session_state, st)
            handle_guess(st.session_state, letter, st)

    with col2:
        display_hangmen(st.session_state, st)
        
    if st.session_state.letter:
        check_game_over(st.session_state, st)
    
    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game(st.session_state, st)

if __name__ == "__main__":
    main()
