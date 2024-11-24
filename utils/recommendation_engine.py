
import os 
from openai import OpenAI

os.getenv('OPENAI_API_KEY')
client = OpenAI()
def get_recommendations(name, age, hobbies, routine, time, interests):
    prompt = f"Suggest hobbies for {name}, aged {age}, who enjoys {', '.join(hobbies)} and has a routine of {routine}. They have {time} minutes available and are interested in {', '.join(interests)}."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that provides hobby recommendations based on user details. You are striclty providing the answer related to that"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()



