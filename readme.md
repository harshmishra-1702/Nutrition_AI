# AI Nutrition Coach - Smart Meal Analyzer

An interactive, multimodal web application built with Flask and the Groq API that allows users to upload images of meals and receive instant nutritional breakdowns, calorie estimations, and dietary feedback. The application includes dynamic analysis modes and session-based conversation memory.

## Features

- **Multimodal Analysis**: Upload an image of a meal alongside a text prompt to analyze nutritional content using advanced vision LLMs.
- **Dynamic Analysis Modes**:
  - *Detailed Breakdown*: Provides identification, itemized portion sizes, precise calorie estimates, total calories, a full macronutrient breakdown, and a comprehensive health evaluation.
  - *Quick Calorie Check*: Offers a streamlined, high-speed response containing just food identification and a total calorie estimate in under three bullet points.
- **Conversation Memory**: Maintains continuous context across subsequent queries, allowing users to ask follow-up questions about their meals without re-uploading the image.
- **Robust Markdown Parsing**: Converts raw model output into clean, structured HTML layouts using a server-side Markdown parser.
- **Minimalist UI**: Modern, clean digital aesthetic featuring side-by-side control panels, a responsive chat stage, live image previews, and embedded loading states.

---

## Tech Stack

- **Backend**: Python, Flask
- **LLM Provider**: Groq SDK (`meta-llama/llama-4-scout-17b-16e-instruct`)
- **Formatting**: Python-Markdown (with `extra` extensions)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla ES6)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai-nutrition-coach
2. Set Up a Virtual Environment
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install flask groq python-markdown python-dotenv
4. Configure Environment Variables
Create a .env file in the root directory of your project and populate it with your Groq API key:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
5. Run the Application
Bash
python app.py
Open your web browser and navigate to http://1270.0.1:5000/ to use the interface.

Project Structure
Plaintext
├── app.py                  # Flask application server & API configuration
├── .env                    # Protected environment variables (API Keys)
├── templates/
│   └── index.html          # Core frontend application layout & chat logic
└── static/
    └── style.css           # Minimalist interface styles & typography