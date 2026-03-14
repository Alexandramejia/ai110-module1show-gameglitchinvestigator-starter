import random
import streamlit as st

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50   # FIX: corrected difficulty range after AI review
    if difficulty == "Hard":
        return 1, 100  # FIX: swapped incorrect ranges with AI suggestion
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"  # FIX: corrected hint direction with AI help
        else:
            return "Too Low", "📈 Go HIGHER!"  # FIX: fixed reversed hint logic
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


# FIX: simplified scoring after AI pointed out inconsistent pattern
def update_score(current_score: int, outcome: str, attempt_number: int):
    return current_score - 10

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 8, # FIX: changed from 6 after AI review
    "Normal": 6, # FIX: changed from 8 after AI review
    "Hard": 5,
} 
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "games" not in st.session_state:
    st.session_state.games = {} # FIX: use separate session state for each difficulty

def new_game_state(low, high):
    return {
        "secret": random.randint(low, high), # FIX: stored secret in session state so it stays stable on rerun
        "attempts": 0,
        "score": 110,  # FIX: start score higher so it decreases each guess
        "status": "playing",
        "history": [],
        "guess_count": 0,
        "last_result": None,
    }

if difficulty not in st.session_state.games:
    st.session_state.games[difficulty] = new_game_state(low, high) # FIX: create new state for each difficulty

game = st.session_state.games[difficulty]

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - game['attempts']}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", game["secret"])
    st.write("Attempts:", game["attempts"])
    st.write("Score:", game["score"])
    st.write("Difficulty:", difficulty)
    st.write("History:", game["history"])

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}_{game['guess_count']}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.games[difficulty] = new_game_state(low, high) # FIX: reset full game state instead of partial reset
    st.session_state.games[difficulty]["last_result"] = {"type": "success", "text": "New game started!"}  
    game = st.session_state.games[difficulty]
    st.rerun()

if game["status"] != "playing":
    if game["status"] == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    game["guess_count"] += 1   # FIX: reset input field after each guess

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        game["history"].append(raw_guess)
        game["last_result"] = {"type": "error", "text": err}
    else:
        game["attempts"] += 1
        game["history"].append(guess_int)

        outcome, message = check_guess(guess_int, game["secret"])

        game["score"] = update_score(
            current_score=game["score"],
            outcome=outcome,
            attempt_number=game["attempts"],
        )

        if outcome == "Win":
            game["status"] = "won"
            game["last_result"] = {
                "type": "success",
                "text": f"You won! The secret was {game['secret']}. Final score: {game['score']}",
                "balloons": True,
            }
        else:
            if game["attempts"] >= attempt_limit:
                game["status"] = "lost"
                game["last_result"] = {
                    "type": "error",
                    "text": f"Out of attempts! The secret was {game['secret']}. Score: {game['score']}",
                }
            elif show_hint:
                game["last_result"] = {"type": "warning", "text": message}  # FIX: only show hints when checkbox is enabled

    st.rerun()

if game["last_result"]:
    r = game["last_result"]
    if r["type"] == "warning":
        if show_hint:
            st.warning(r["text"])
    elif r["type"] == "error":
        st.error(r["text"])
    elif r["type"] == "success":
        if r.get("balloons"):
            st.balloons()
        st.success(r["text"])

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
