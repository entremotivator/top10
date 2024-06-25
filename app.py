import streamlit as st
import pandas as pd
from datetime import datetime, date

# 1. Dashboard
def dashboard():
    st.title("Dashboard")
    st.write("Overview of activities")

    # Example metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Sessions Completed", "15", "5")
    col2.metric("Active Users", "120", "10")
    col3.metric("New Users", "30", "3")

    # Example progress chart using Streamlit's line_chart
    st.subheader("Progress Overview")
    dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
    progress = [5, 6, 7, 8, 7, 9, 10, 12, 14, 15, 18, 20]
    progress_df = pd.DataFrame({"Date": dates, "Sessions": progress})
    st.line_chart(progress_df.set_index("Date"))

# 2. User Profile
def user_profile():
    st.title("User Profile")

    # Example user details form
    st.subheader("Personal Information")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", 18, 100)
    bio = st.text_area("Bio")

    if st.button("Save"):
        st.success("Profile updated successfully!")

# 3. Coach Profile
def coach_profile():
    st.title("Coach Profile")

    # Example coach profile display
    st.subheader("Coach Information")
    st.write("Name: Jane Doe")
    st.write("Expertise: Fitness, Nutrition")
    st.write("Experience: 10 years")
    st.write("Availability: Mon-Fri, 9 AM - 5 PM")

    # Example coach selection
    coaches = ["Jane Doe", "John Smith", "Emily Johnson"]
    selected_coach = st.selectbox("Select a coach", coaches)
    st.write(f"You selected: {selected_coach}")

# 4. Session Scheduling
def session_scheduling():
    st.title("Session Scheduling")

    # Example session scheduling form
    st.subheader("Schedule a Session")
    selected_date = st.date_input("Select date", date.today())
    selected_time = st.time_input("Select time", datetime.now().time())
    st.write(f"Session scheduled for {selected_date} at {selected_time}")

    if st.button("Confirm"):
        st.success(f"Session confirmed for {selected_date} at {selected_time}")

# 5. Progress Tracking
def progress_tracking():
    st.title("Progress Tracking")

    # Example progress tracking input
    st.subheader("Track your progress")
    progress_date = st.date_input("Date", date.today())
    progress_description = st.text_area("Description of progress")

    if st.button("Add Progress"):
        st.success("Progress added successfully!")

# 6. Communication Tools
def communication_tools():
    st.title("Communication Tools")

    # Example in-app messaging
    st.subheader("Message your coach")
    message = st.text_area("Enter your message")

    if st.button("Send Message"):
        st.success("Message sent successfully!")

# 7. Resource Library
def resource_library():
    st.title("Resource Library")

    # Example resource display
    st.subheader("Available Resources")
    resources = ["Article 1: Nutrition Basics", "Video: Effective Workouts", "Exercise Plan: Beginner"]
    for resource in resources:
        st.write(resource)

# 8. Feedback System
def feedback_system():
    st.title("Feedback System")

    # Example feedback form
    st.subheader("Provide Feedback")
    session_feedback = st.text_area("Feedback on your session")

    if st.button("Submit Feedback"):
        st.success("Feedback submitted successfully!")

# 9. Analytics and Reporting
def analytics_reporting():
    st.title("Analytics and Reporting")

    # Example analytics display using Streamlit's bar_chart
    st.subheader("User Engagement")
    engagement_data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sessions": [5, 7, 8, 10, 12]
    }
    engagement_df = pd.DataFrame(engagement_data)
    st.bar_chart(engagement_df.set_index("Month"))

# 10. Navigation
st.sidebar.title("Navigation")
options = ["Dashboard", "User Profile", "Coach Profile", "Session Scheduling", "Progress Tracking", "Communication Tools", "Resource Library", "Feedback System", "Analytics and Reporting"]
choice = st.sidebar.selectbox("Go to", options)

if choice == "Dashboard":
    dashboard()
elif choice == "User Profile":
    user_profile()
elif choice == "Coach Profile":
    coach_profile()
elif choice == "Session Scheduling":
    session_scheduling()
elif choice == "Progress Tracking":
    progress_tracking()
elif choice == "Communication Tools":
    communication_tools()
elif choice == "Resource Library":
    resource_library()
elif choice == "Feedback System":
    feedback_system()
elif choice == "Analytics and Reporting":
    analytics_reporting()

