def handle_guess(state, letter, st):
    if letter.isalpha():
        if letter in state.letters_tried:
            st.warning(f"You have already guessed '{letter}'")
        else:
            state.letters_tried.append(letter)
            if letter not in state.word:
                state.letters_wrong += 1
                st.error(f"'{letter}' is not in the word.")
            else:
                st.success(f"Good job! '{letter}' is correct.")
                for i, char in enumerate(state.word):
                    if char == letter:
                        state.clue[i] = letter
    elif letter:
        st.warning("Please enter a valid single letter.")

def display_guessed_letters(state, st):
    st.write("Guessed letters: " + ", ".join(state.letters_tried))