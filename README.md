Step-by-Step Instructions
## 1. Clone the Repository
First, clone the repository containing your project to your local machine. Open your terminal and run:

sh
git clone https://github.com/pranavsane/HOBBY_RECCOMENDATION_APP.git
##  2. Navigate to the Project Directory
Change to the project directory:

sh
cd hobby-recommendation-app
## 3. Set Up a Virtual Environment (Optional but Recommended)
It's a good practice to use a virtual environment to manage your project dependencies. You can create and activate a virtual environment with the following commands:

sh
# Create a virtual environment (on Unix-based systems)
python3 -m venv venv

# Activate the virtual environment (on Unix-based systems)
source venv/bin/activate

# Create a virtual environment (on Windows)
python -m venv venv

# Activate the virtual environment (on Windows)
.\venv\Scripts\activate

## 4. Install Dependencies
Install all the required dependencies listed in requirements.txt:

sh
pip install -r requirements.txt
## 5. Set Up OpenAI API Key
Ensure you have your OpenAI API key. You can get your API key by signing up at OpenAI. Once you have your API key, set it in the environment variable. You can do this directly in your terminal:

sh
export OPENAI_API_KEY='your-openai-api-key'  # For Unix-based systems

set OPENAI_API_KEY='your-openai-api-key'  # For Windows
Alternatively, you can set your API key directly in the code:

python
openai.api_key = 'your-openai-api-key'

## 6. Create Data Directory (if it doesn't exist)
Make sure the data directory exists for storing user data:

sh
mkdir -p data


## 7. Run the Streamlit App
Start the Streamlit app by running the following command:

sh
streamlit run main.py


## 8. Interact with the App
Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

Enter your user information in the sidebar, including name, age, current hobbies, routine, available time, and interests.

Click the "Get Recommendations" button to generate hobby suggestions and save your details.

## 9. Review Saved User Data
The user data is saved to the data/users.csv file. You can open this file to review the saved entries.

Stopping the Application
To stop the Streamlit app, go to the terminal where it's running and press Ctrl + C.

By following these steps, you should be able to set up, run, and interact with the Hobby Recommendation App on your local machine. If you encounter any issues or have any questions, feel free to reach out! 🚀
