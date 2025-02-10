from random_word import get_word
from graphics import celebration_animations


def check_game_over(state, st):
    if state.letters_wrong == 6:
        state.game_over = True
        st.write(f"The word was: {state.word}")
        st.image("gif.gif", use_container_width=True)
    
    if "".join(state.clue) == state.word:
        state.game_over = True
        st.markdown("# Congratulations")
        st.write(f"The word was: {state.word}")
        st.balloons()
        celebration_animations()

def reset_game(state, st):
    state.word, state.hint = get_word()
    state.clue = ["-"] * len(state.word)
    state.letters_tried = []
    state.letters_wrong = 0
    state.game_over = False
    state.hint_offered = False
    st.rerun()