import streamlit as st
import random
import pandas as pd
from transformers import pipeline

# Sample leaderboard data (in a real app, this would be stored in a database)
leaderboard = pd.DataFrame({
    'User': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Points': [150, 120, 100, 90],
    'Community Bonus': [20, 15, 10, 5]
})

def generate_challenge(goals, constraints):
    pipe = pipeline("text-generation",
                    model="google/gemma-2-2b-it",
                    max_new_tokens=50
                    )
    prompt = f"Generate a sustainability challenge based on the following goals: {goals} and constraints: {constraints}."
    messages = [{"role": "user", "content": prompt}]
    # output = pipe(messages)
    # [0]['generated_text']
    # print("Output:", output)
    # challenge = output.replace(prompt, "").strip()
    # print("Challenge:", challenge)
    challenges = [
        "Reduce your water usage by 10% this week.",
        "Start composting at home and reduce food waste.",
        "Try using public transportation instead of driving for 3 days.",
        "Set up a recycling system at home and reduce waste.",
        "Switch to energy-efficient light bulbs and reduce energy consumption."
        "Plant a tree in your community.",
        "Organize a neighborhood clean-up event.",
        "Reduce your plastic usage by switching to reusable items.",
        "Install a rainwater harvesting system.",
        "Use a clothesline instead of a dryer to save energy.",
        "Participate in a local environmental workshop.",
        "Switch to a plant-based diet for a week.",
        "Reduce your meat consumption by half.",
        "Use eco-friendly cleaning products.",
        "Support local farmers by buying locally grown produce.",
        "Reduce your paper usage by going digital.",
        "Carpool with colleagues to reduce carbon emissions.",
        "Implement a home energy audit to identify savings.",
        "Reduce your shower time to save water.",
        "Use a reusable water bottle instead of disposable ones.",
        "Donate old clothes and items instead of throwing them away.",
        "Switch to a green energy provider.",
        "Reduce your thermostat by 2 degrees in winter.",
        "Unplug electronics when not in use to save energy.",
        "Educate others about sustainability practices."
    ]
    
    # Filter challenges based on user input (goals and constraints)
    # For simplicity, let's just select a random challenge (can be expanded based on real logic)
    challenge = random.choice(challenges)
    
    if 'waste' in goals or 'reduce' in constraints:
        challenge = "Start composting at home and reduce food waste."
    
    if 'energy' in goals:
        challenge = "Switch to energy-efficient light bulbs and reduce energy consumption."

    return challenge

def update_leaderboard(user, points, community_bonus):
    global leaderboard
    new_entry = pd.DataFrame([[user, points, community_bonus]], columns=['User', 'Points', 'Community Bonus'])
    leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
    leaderboard = leaderboard.sort_values(by=['Points', 'Community Bonus'], ascending=False)
    leaderboard = leaderboard.reset_index(drop=True)

st.title("Sustainability Challenge Chatbot with Leaderboard")

# Section 1: Input for user goals and constraints
st.header("Tell Us Your Sustainability Goals & Constraints")
goals_input = st.text_input("What are your sustainability goals? (e.g., reduce waste, save energy, go green, etc.)")
constraints_input = st.text_input("Any constraints? (e.g., limited time, budget, space, etc.)")

try:
    if st.button("Generate Challenge"):
        st.subheader("Your Personalized Sustainability Challenge")
        # Generate a challenge based on goals and constraints using Gemma
        challenge = generate_challenge(goals_input, constraints_input)
        st.write(challenge)
        
        # Input for challenge completion
        st.subheader("Did you complete this challenge?")
        completed = st.radio("Have you completed this challenge?", ["Yes", "No"])
        
        if completed == "Yes":
            st.write("Great job! Keep it up!")
            
            # Input for user to enter their name and points
            user_name = st.text_input("Enter your name:", key="name")
            if user_name:
                points = random.randint(10, 50)  # Random points for completion (could be customized)
                community_bonus = random.randint(1, 20)  # Simulate community bonus for leaderboard
                update_leaderboard(user_name, points, community_bonus)
                st.write(f"Congratulations, {user_name}! You earned {points} points and {community_bonus} bonus points.")
        else:
            st.write("No worries! You can try again later.")
except Exception as e:
    st.write("Error:", e)

# Section 2: Display Leaderboard
st.header("Leaderboard")
st.write("Top users based on sustainability challenges completed")

# Show the leaderboard with community bonuses
st.write(leaderboard[['User', 'Points', 'Community Bonus']])

