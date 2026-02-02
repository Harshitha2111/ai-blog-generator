import markdown
from flask import Flask, render_template, request, session
import os
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ NEW
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


load_dotenv()

app = Flask(__name__)

# ✅ SESSION SECRET
app.secret_key = os.getenv("FLASK_SECRET", "change_this_secret")

# ✅ RATE LIMITER
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)

# ✅ Configure GEMINI_API_KEY safely
genai.api_key = os.environ.get("GEMINI_API_KEY")

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
    response = model.generate_content(prompt)

    if not response or not hasattr(response, "text") or not response.text:
        raise RuntimeError("Gemini returned empty response")

    return response.text.strip()


@app.route("/", methods=["GET", "POST"])
@limiter.limit("3 per minute")
def index():
    blog = ""

    # ✅ SESSION CONTROL
    if "count" not in session:
        session["count"] = 0

    if request.method == "POST":
        session["count"] += 1

        if session["count"] > 5:
            return "Too many requests. Please wait a minute and refresh."

        data = {
            "topic": request.form.get("topic", "").strip(),
            "purpose": request.form.get("purpose", "").strip(),
            "audience": request.form.get("audience", "").strip(),
            "tone": request.form.get("tone", "Professional"),
            "length": request.form.get("length", "medium"),
            "keywords": request.form.get("keywords", "").strip(),
        }

        if not data["topic"]:
            blog = "❌ ERROR: Topic is required."
        else:
            try:
                prompt = build_prompt(data)
                raw_blog = generate_blog(prompt)
                blog = markdown.markdown(raw_blog)

            except Exception as e:
                blog = f"❌ Blog generation failed: {str(e)}"

    return render_template("index.html", blog=blog)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
