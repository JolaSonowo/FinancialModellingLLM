from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Flask and OpenAI client
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def expand_query(query: str) -> str:
    """
    Expands a user query using OpenAI GPT API.

    Args:
        query (str): The user input query.

    Returns:
        str: Expanded query text or error message.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial assistant."},
                {"role": "user", "content": f"Expand and clarify this query: {query}"}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/expand", methods=["POST"])
def expand():
    """API endpoint to expand a query."""
    data = request.json
    query = data.get("query", "")
    expanded_query = expand_query(query)
    return jsonify({"expanded_query": expanded_query})

if __name__ == "__main__":
    app.run(debug=True)
