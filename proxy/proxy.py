from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import openai
import os
from flask_cors import CORS, cross_origin

load_dotenv()
client = OpenAI()

app = Flask(__name__)
CORS(app)

@app.route('/get_poem', methods=['POST'])
@cross_origin()
def get_poem():
    try:
        data = request.json
        user_message = data.get('user_message', '')
        print("-" * 50)
        print("Received user message:", user_message)
        print("-" * 50)

        # Set a timeout for the OpenAI API request (adjust the value as needed)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user", "content": user_message}
            ],
        )
        print("Received response from OpenAI:", completion)
        response = completion.choices[0].message.content
        print("Generated response:", response)
        return jsonify({'response': response})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500  # Return a 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
