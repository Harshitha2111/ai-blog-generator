from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print("🔥 RUNNING THIS app.py FILE 🔥")

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ USE A KNOWN WORKING MODEL
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are an expert professional blog writer."
)


def build_prompt(data: dict) -> str:
    prompt = f"""
Write a {data['tone']} blog.

Topic:
{data['topic']}

Purpose of the blog:
{data['purpose']}

Target audience:
{data['audience']}

Length:
{data['length']} (short ≈ 500 words, medium ≈ 800 words, long ≈ 1200 words)

SEO Keywords to include naturally:
{data['keywords']}

Guidelines:
- Clear structure with headings
- Engaging introduction
- Informative and practical
- Professional language
- Avoid emojis
"""
    return prompt.strip()


def generate_blog(prompt: str) -> str:
    print("🟡 SENDING PROMPT TO GEMINI...")
    print(prompt)

    response = model.generate_content(prompt)

    # ✅ HARD VALIDATION (NO SILENT FAILURES)
    if not response:
        raise RuntimeError("Gemini returned no response")

    if not hasattr(response, "text") or not response.text:
        raise RuntimeError("Gemini response text is empty")

    print("🟢 GEMINI RESPONSE RECEIVED")
    return response.text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    blog = ""

    if request.method == "POST":
        print("📥 FORM SUBMITTED")
        print("RAW FORM DATA:", request.form)

        data = {
            "topic": request.form.get("topic", "").strip(),
            "purpose": request.form.get("purpose", "").strip(),
            "audience": request.form.get("audience", "").strip(),
            "tone": request.form.get("tone", "Professional"),
            "length": request.form.get("length", "medium"),
            "keywords": request.form.get("keywords", "").strip(),
        }

        print("📦 PARSED DATA:", data)

        if not data["topic"]:
            blog = "❌ ERROR: Topic is required."
        else:
            try:
                prompt = build_prompt(data)
                blog = generate_blog(prompt)
            except Exception as e:
                print("🔴 ERROR:", e)
                blog = f"❌ Blog generation failed: {str(e)}"

    return render_template("index.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)