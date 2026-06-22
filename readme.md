# AI Nutrition Coach 🥗

AI Nutrition Coach is an intelligent, interactive web-based nutrition analysis platform developed using Flask, Python, and advanced Multimodal Large Language Models. It transforms simple meal images into detailed nutritional insights, providing instant calorie estimation, macronutrient breakdowns, and personalized dietary feedback.

Instead of relying on manual calorie tracking or generic food databases, the system utilizes powerful vision-enabled AI models to understand meal composition, estimate portion sizes, and generate structured health evaluations through a conversational interface.



---

## 🛠️ Key Architecture & System Features

* **Intelligence Engine:** Powered by Groq's high-speed LPU inference system running the `meta-llama/llama-4-scout-17b-16e-instruct` multimodal model for advanced food image understanding and nutritional reasoning.

* **Vision Analysis Layer:** Enables users to upload meal images and combines visual recognition with user prompts to identify food items, estimate serving quantities, analyze calories, and provide detailed dietary recommendations.

* **Adaptive Nutrition Modes:** Implements multiple AI response pipelines including:
  - **Detailed Breakdown:** Generates item-wise food identification, portion estimation, calorie calculation, macronutrient distribution, and overall health assessment.
  - **Quick Calorie Check:** Produces a lightweight instant response focusing on rapid meal identification and approximate calorie estimation.

* **Conversation Memory System:** Maintains session-level context, allowing users to continue discussions, ask follow-up nutrition questions, and receive adaptive feedback without repeatedly uploading images.

* **Response Formatting Engine:** Integrates Python-Markdown processing to convert AI-generated responses into structured, readable HTML layouts with clean formatting and improved readability.

* **Interface Layer:** Designed with HTML5, CSS3, and Vanilla JavaScript featuring a minimalist dashboard, real-time image preview system, responsive chat interface, interactive controls, and smooth loading indicators.



---

## 💻 Technology Stack

* **Backend Framework:** Flask (Python)
* **AI Provider:** Groq SDK
* **AI Model:** `meta-llama/llama-4-scout-17b-16e-instruct`
* **Frontend Layer:** HTML5, CSS3, JavaScript (Vanilla ES6)
* **Markdown Renderer:** Python-Markdown (`extra` extensions)
* **Environment Management:** Python-dotenv



---

## 🚀 Installation & Setup Guide

Follow these sequential steps to configure and execute the application locally.



### 1. Clone or Structure the Project Files

Ensure your root workspace contains the required development files:

```plaintext
AI_Nutrition_Coach/
│
├── .env                  # Environment configuration file (Hidden)
├── .gitignore            # Version control exclusion rules
├── app.py                # Flask application server & AI API logic
├── requirements.txt      # Python dependency configuration
│
├── templates/
│   └── index.html        # Frontend layout and client interaction logic
│
└── static/
    └── style.css         # Interface styling and responsive design
```



### 2. Establish and Activate a Virtual Environment

Open your terminal inside the project directory and create an isolated Python workspace.

**On Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```



### 3. Install Package Dependencies

Install all required libraries from the dependency configuration file:

```bash
pip install -r requirements.txt
```



### 4. Configure Secure Environment Variables

Create a file named `.env` inside the root project directory.

Add your Groq API authentication key:

```text
GROQ_API_KEY="your_actual_groq_api_key_here"
```

> ⚠️ **Important Security Note:**  
> Generate your API key from the official Groq Cloud Console.  
> Never expose your `.env` file or upload private API credentials to public repositories.



---

## 🖥️ Running the Application

After completing the setup process and activating your virtual environment, start the Flask development server using:

```bash
python app.py
```

The application will initialize a local server.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Upload a meal image, select your preferred analysis mode, enter optional instructions, and allow the AI Nutrition Coach to generate intelligent nutritional insights instantly.

---

## ✨ Application Workflow

```plaintext
User Uploads Meal Image
            ↓
Image + Prompt Processing
            ↓
Groq Multimodal Vision Model
            ↓
AI Nutrition Interpretation
            ↓
Markdown Response Formatting
            ↓
Interactive Nutrition Dashboard
```
