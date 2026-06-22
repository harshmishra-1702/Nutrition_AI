import os
import base64
import json
import markdown
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

MODEL_ID = "meta-llama/llama-4-scout-17b-16e-instruct"

def format_response(response_text):
    return markdown.markdown(response_text, extensions=['extra'])

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.form.get("user_query", "Analyze this meal.")
    mode = request.form.get("mode", "detailed")
    
    try:
        history = json.loads(request.form.get("history", "[]"))
    except json.JSONDecodeError:
        history = []
        
    uploaded_file = request.files.get("file")
    encoded_image = None
    
    if uploaded_file and uploaded_file.filename != '':
        bytes_data = uploaded_file.read()
        encoded_image = base64.b64encode(bytes_data).decode("utf-8")

    if mode == "quick":
        assistant_prompt = """
        You are a fast, efficient AI Nutrition Coach. Look at the image or context and provide ONLY two things:
        1. **Identification**: What is the food?
        2. **Quick Estimate**: What is the estimated portion size and total calorie count?
        Keep it to a maximum of 3 bullet points. Do NOT provide macro breakdowns or health evaluations.
        """
    else:
        assistant_prompt = """
        You are an expert nutritionist. Analyze the food items and provide a detailed nutritional assessment using this format:
        1. **Identification**: List each identified food item clearly.
        2. **Portion Size & Calorie Estimation**: Specify portion size and estimated calories.
        3. **Total Calories**: Provide the total number of calories.
        4. **Nutrient Breakdown**: Include Protein, Carbohydrates, Fats, Vitamins, Minerals.
        5. **Health Evaluation**: Evaluate the healthiness in one paragraph.
        6. **Disclaimer**: State that the information is approximate.
        """

    messages = [{"role": "system", "content": assistant_prompt}]
    
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})
        
    current_message_content = []
    
    if encoded_image:
        current_message_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
        })
        
    current_message_content.append({"type": "text", "text": user_query})
    messages.append({"role": "user", "content": current_message_content})

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=MODEL_ID,
            temperature=0.2 
        )
        
        raw_response = chat_completion.choices[0].message.content
        formatted_response = format_response(raw_response)
        
        return jsonify({"response": formatted_response})

    except Exception as e:
        print(f"Inference error: {e}")
        return jsonify({"error": "Failed to process the request."}), 500

if __name__ == "__main__":
    app.run(debug=True)