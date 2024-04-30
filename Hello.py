# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

# Placeholder for user database
# In a real application, this should be replaced with a proper database and secure password handling
users_db = {}

# Function to save user account (simple dictionary for demonstration)
def create_user(username, password):
    users_db[username] = password
    return "User created successfully"

# Function to check user credentials
def check_user(username, password):
    if username in users_db and users_db[username] == password:
        return True
    return False

# Main app layout with account system
def main_app():
    tab1, tab2, tab3 = st.tabs(["User Info", "Fitness Target", "Daily Log"])

    with tab1:
        user_info_form()

    with tab2:
        fitness_target_form()

    with tab3:
        daily_log_form()

# Login system layout
def login_system():
    st.subheader("Welcome to the Fitness Tracker App")
    
    # Account actions
    account_action = st.radio("Choose an action:", ("Login", "Create Account"))
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if account_action == "Create Account":
        if st.button("Create Account"):
            message = create_user(username, password)
            st.success(message)
    elif account_action == "Login":
        if st.button("Login"):
            if check_user(username, password):
                st.success(f"Logged in as {username}")
                main_app()  # Load main app after successful login
            else:
                st.error("Invalid username or password")

# Function to display User Information form
def user_info_form():
    with st.form("user_info", clear_on_submit=True):
        st.subheader("User Information")
        user_name = st.text_input("Name")
        user_height = st.number_input("Height (in cm)")
        user_weight = st.number_input("Weight (in kg)")
        user_body_fat = st.number_input("Body Fat Percentage (%)")
        user_age = st.number_input("Age")
        user_gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
        submit_user = st.form_submit_button("Submit User Info")
        if submit_user:
            st.success("User Information Saved")

# Function to display Set Fitness Target form
def fitness_target_form():
    with st.form("fitness_target", clear_on_submit=True):
        st.subheader("Set Fitness Target")
        target_weight = st.number_input("Target Weight (in kg)")
        calories_intake = st.number_input("Daily Caloric Intake")
        carbs_intake = st.number_input("Daily Carbs Intake (in grams)")
        protein_intake = st.number_input("Daily Protein Intake (in grams)")
        fat_intake = st.number_input("Daily Fat Intake (in grams)")
        submit_target = st.form_submit_button("Submit Fitness Target")
        if submit_target:
            st.success("Fitness Target Set")

# Function to display Daily Log form
def daily_log_form():
    with st.form("daily_log", clear_on_submit=True):
        st.subheader("Daily Log")
        meals_consumed = st.text_area("Meals Consumed")
        exercises_done = st.text_area("Exercises Done")
        calories_burned = st.number_input("Total Calories Burned")
        notes = st.text_area("Notes")
        submit_log = st.form_submit_button("Submit Daily Log")
        if submit_log:
            st.success("Daily Log Saved")

# Display the login system as the starting point of the app
if __name__ == "__main__":
    login_system()
