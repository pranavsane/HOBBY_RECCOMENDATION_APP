import csv
import os
import streamlit as st
from utils.recommendation_engine import get_recommendations


# Title and Sidebar
st.title('Hobby Recommendation App')
st.sidebar.header('User Information')

# Collecting user information
name = st.sidebar.text_input('Name')
age = st.sidebar.number_input('Age', min_value=1, max_value=100, value=25)
hobbies = st.sidebar.multiselect('Current Hobbies', ['Painting', 'Drawing', 'Writing', 'Music (playing an instrument, composing, singing)', 'Photography', 'Video Editing', 'Digital Art', 'DIY Crafts', 'Cooking', 'Baking', 'Gardening', 'Homebrewing', 'Board Games', 'Puzzles', 'Card Games', 'Hiking', 'Camping', 'Rock Climbing', 'Kayaking', 'Surfing', 'Fishing', 'Birdwatching', 'Cycling', 'Running', 'Yoga', 'Pilates', 'Meditation', 'Reading', 'Learning a new language', 'Coding', 'Playing chess', 'Solving puzzles', 'Watching documentaries', 'Attending lectures and workshops', 'Volunteering', 'Joining clubs and groups', 'Playing team sports', 'Board game nights', 'Book clubs', 'Movie nights'])
routine = st.sidebar.text_area('Describe your daily routine')
available_time = st.sidebar.slider('Available Time (minutes)', 5, 60, 15)
interests = st.sidebar.multiselect('Interests', ['Physical Activities', 'Intellectual' ,'Creative Hobbies', 'Social Challenges'])

# Function to append user data to CSV
def append_user_data(filepath, data):
    file_exists = os.path.isfile(filepath)
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Age', 'Hobbies', 'Routine', 'Available Time', 'Interests'])  # Write header
        writer.writerow(data)

# Button to get recommendations and save user data
if st.sidebar.button('Get Recommendations'):
    recommendations = get_recommendations(name, age, hobbies, routine, available_time, interests)
    st.write(f'Hello {name}, here are your hobby suggestions:')
    st.write(recommendations)
    
    # Save user data to CSV
    user_data = [name, age, ', '.join(hobbies), routine, available_time, ', '.join(interests)]
    append_user_data('data/users.csv', user_data)
    st.success('Your information has been saved!')
