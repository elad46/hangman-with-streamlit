import streamlit as st
import random
import string
import pandas as pd

animals = ["dog", "cat", "elephant", "lion", "tiger", "bear", "rabbit", "monkey"]
technology = ["computer", "python", "programming", "internet", "game", "code", "software", "hardware"]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "white"]
objects = ["table", "chair", "book", "pen", "bag", "glasses", "phone", "keyboard"]
food = ["pizza", "burger", "apple", "banana", "chocolate", "coffee", "sandwich", "cake"]

SETS = {
    "All": animals + technology + colors + objects + food,
    "Animals": animals,
    "Technology": technology,
    "Colors": colors,
    "Objects": objects,
    "Food": food,
}

# איתחול session state לניווט ניקוד, רמז ושם שחקן
if "scoreboard" not in st.session_state:
    st.session_state.scoreboard = {}
if "score_updated" not in st.session_state:
    st.session_state.score_updated = False
if "hint_shown" not in st.session_state:
    st.session_state.hint_shown = False
if "player_name" not in st.session_state:
    st.session_state.player_name = "Player"

st.set_page_config(page_title="Simple Hangman", page_icon="🎮", layout="centered")
st.title("🎮 Simple Hangman.")

def choose_random_word(words):
    return random.choice(words).upper()

def masked_word(secret, guessed):
    return " ".join(ch if ch in guessed or not ch.isalpha() else "_" for ch in secret)

def start_new_game(wordset_name, max_mistakes):
    # אתחול משחק חדש וreset flags
    secret = choose_random_word(SETS[wordset_name])
    st.session_state.game = {
        "secret": secret,
        "guessed": set(),
        "mistakes": 0,
        "max_mistakes": max_mistakes,
        "final_mode": False,  # צ'אנס אחרון לניחוש מלא
        "over": False,
        "win": False,
    }
    st.session_state.score_updated = False
    st.session_state.hint_shown = False

def ensure_game():
    if "game" not in st.session_state:
        start_new_game("All", 5)

def guess_letter(letter):
    g = st.session_state.game
    if g["over"] or g["final_mode"]:
        return
    letter = letter.upper()
    if not letter.isalpha() or len(letter) != 1 or letter in g["guessed"]:
        return

    g["guessed"].add(letter)
    if letter not in g["secret"]:
        g["mistakes"] += 1

    # בדיקת סיום
    if all((not ch.isalpha()) or (ch in g["guessed"]) for ch in g["secret"]):
        g["win"] = True
        g["over"] = True
        st.balloons()
    elif g["mistakes"] >= g["max_mistakes"]:
        g["final_mode"] = True  # טעויות נגמרו + צ'אנס אחרון

def guess_full(word):
    g = st.session_state.game
    if g["over"]:
        return
    candidate = (word or "").strip().upper()
    if candidate == g["secret"]:
        g["win"] = True
        g["over"] = True
        st.balloons()
    else:
        g["mistakes"] += 1
        g["win"] = False
        g["over"] = True
        st.snow()

def get_category(secret):
    # מחזיר את שם הקטגוריה שאליה שייכת המילה
    for name, words in SETS.items():
        if name == "All":
            continue
        # השוואה ללא תלות באותיות גדולות/קטנות
        if secret.lower() in [w.lower() for w in words]:
            return name
    return "Unknown"

# לוודא שיש משחק פעיל
ensure_game()
g = st.session_state.game

# Sidebar – הגדרות, רמזים ולוח תוצאות
with st.sidebar:
    st.header("Settings")
    # שם שחקן
    player_name = st.text_input("Player name", value=st.session_state.player_name)
    st.session_state.player_name = player_name

    set_name = st.selectbox("Word set", list(SETS.keys()), index=0)
    max_mistakes = st.slider("Max mistakes", 1, 10, g["max_mistakes"] if "game" in st.session_state else 5)
    if st.button("🎲 New Game"):
        start_new_game(set_name, max_mistakes)

    # כפתור להצגת רמז
    if st.button("Show hint"):
        st.session_state.hint_shown = True

    # הצגת רמז (קטגוריה של המילה) אם נלחץ
    if st.session_state.hint_shown:
        cat = get_category(g["secret"])
        st.info(f"Hint: The word is from the **{cat}** category.")

    # לוח תוצאות
    st.subheader("Leaderboard")
    if st.session_state.scoreboard:
        df_scores = pd.DataFrame(
            list(st.session_state.scoreboard.items()),
            columns=["Player", "Score"]
        ).sort_values("Score", ascending=False)
        st.table(df_scores)
    else:
        st.write("No scores yet.")

# תוכן עיקרי של המשחק
st.subheader("Status")
st.write(f"Mistakes: **{g['mistakes']} / {g['max_mistakes']}**")
st.write("Word:")
st.write(f"**{masked_word(g['secret'], g['guessed'])}**")

st.write("Guess a letter:")
alphabet = list(string.ascii_uppercase)

def chunk(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

for row in chunk(alphabet, 9):
    cols = st.columns(len(row))
    for i, letter in enumerate(row):
        disabled = (letter in g["guessed"]) or g["over"] or g["final_mode"]
        if cols[i].button(letter, key=f"k_{letter}", disabled=disabled):
            guess_letter(letter)

# במצב "צ'אנס אחרון" – ניחוש מלא
if g["final_mode"] and not g["over"]:
    st.info("Last chance! Guess the full word:")
    with st.form("full_form", clear_on_submit=True):
        full = st.text_input("Full word (UPPER/lowercase doesn't matter)")
        done = st.form_submit_button("Submit")
        if done and full:
            guess_full(full)

# הודעת סיום והעברת ניקוד ללוח התוצאות
if g["over"]:
    if g["win"]:
        st.success(f"🎉 You win! The word was: {g['secret']}")
    else:
        st.error(f"😿 You lost... The word was: {g['secret']}")

    # עדכון לוח הניקוד (רק פעם אחת לכל משחק)
    if not st.session_state.score_updated:
        name = st.session_state.player_name or "Player"
        # ניקוד על בסיס מספר ניסיונות שנשארו – אפשר לשנות לשיטה אחרת
        score = g["max_mistakes"] - g["mistakes"] if g["win"] else 0
        current = st.session_state.scoreboard.get(name, 0)
        st.session_state.scoreboard[name] = current + score
        st.session_state.score_updated = True