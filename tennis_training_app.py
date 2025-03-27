
import streamlit as st
import time
import datetime

# --- App Setup ---
st.set_page_config(page_title="Tennis Pro Training", layout="centered")
st.title("🎾 Tennis Pro Training Assistant")

# --- Initialize Session State ---
if 'workout_log' not in st.session_state:
    st.session_state.workout_log = []

# --- Custom Timer ---
st.header("⏱️ Custom Workout Timer")
exercise_name = st.text_input("Exercise Name:", "Jump Squats")
duration = st.number_input("Duration (seconds):", min_value=5, max_value=600, value=30)
sets = st.number_input("Number of Sets:", min_value=1, max_value=20, value=4)

auto_log = st.checkbox("Log this workout after completion", value=True)

if st.button("Start Timer"):
    for i in range(sets):
        st.write(f"**Set {i+1}/{sets} — {exercise_name}**")
        with st.empty():
            for seconds in range(duration, 0, -1):
                st.metric(label="Time Remaining", value=f"{seconds}s")
                time.sleep(1)
        st.success(f"✅ Set {i+1} Complete!")
        if i < sets - 1:
            st.info("⏸️ 30s Rest")
            time.sleep(30)
    if auto_log:
        st.session_state.workout_log.append({
            "date": str(datetime.date.today()),
            "exercise": exercise_name,
            "sets": sets,
            "duration": duration
        })
        st.success("✅ Workout Logged!")

# --- Weekly Training Program ---
st.header("📋 Weekly Training Program")
st.markdown("""
This is your 3-day off-court plan with Thera-Band support:

**Day 1 – Explosive Power + Core Stability**
- Jump Squats – 4x10
- Bulgarian Split Squats – 3x10/leg
- Broad Jumps – 3x6
- Skater Bounds – 3x15
- Isometric Wall Sit – 3x45s
- Core: Plank w/ Shoulder Taps, Hollow Hold, Bird Dogs

**Day 2 – Speed, Agility & Reaction**
- Ladder Drills – 4 rounds
- Cone X-Drill – 4x30s
- Reaction Ball Drill – 4x1min
- Jump Lunge + Split Squats – 3x20
- Core Finisher: Russian Twists, Side Planks

**Day 3 – Conditioning + Band Strength**
- HIIT Block: 5x (30s High Knees + 30s Jump Squats)
- 3x (45s Jump Rope + 45s Shadow Tennis + 1min Rest)
- Band Rows (Thera-Band) – 3x15
- Band Chest Press – 3x15
- Band Pallof Press – 3x12 each side
- Band Woodchoppers – 3x12 each side
- Core: Side Plank Reach, Hanging Hold (or Hollow Hold)
""")

# --- Workout Log ---
st.header("📊 Workout History")
if st.session_state.workout_log:
    for entry in reversed(st.session_state.workout_log):
        st.write(f"🗓️ {entry['date']} – {entry['exercise']} – {entry['sets']} sets of {entry['duration']}s")
else:
    st.info("No workouts logged yet. Complete a session above to start tracking!")

# --- Footer ---
st.caption("Designed by ChatGPT & Alessandro for tennis warriors 💪")
