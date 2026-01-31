# AI Blog Generator Agent (Web App)

A hackathon project that implements a web-based **AI Blog Generator Agent** capable of generating complete, structured blog articles with **AI-generated images aligned to each paragraph**.

The application converts a single blog idea into a fully formatted article with relevant visuals, providing an end-to-end AI-powered content creation experience.

**Python | Flask | HTML | CSS | AI Text Generation**

---

## Problem Statement

Build a web-based AI agent that generates complete blog articles from user inputs.  
Each blog must include AI-generated images aligned with the corresponding paragraphs.

---

## Objective

To design and develop a web application that transforms a blog idea into a structured article enriched with AI-generated images, ensuring semantic alignment between text and visuals.

---

## Inputs

- Blog Topic  
- Blog Description (detailed context of the blog)  
- Target Audience  
- Tone (Formal / Informal / Technical / Narrative)  
- Blog Length (Short / Medium / Long)  
- Keywords (Optional)

---

## Outputs

- Blog Title  
- Structured Blog Content  
  - Introduction  
  - Multiple sections / paragraphs  
- AI-Generated Images  
  - At least one image per paragraph  
  - Image placed below the corresponding paragraph  
- Blog Preview Page  
- Exported Blog (HTML / Markdown / PDF – any one)

---

## Functional Requirements

- Generate original, coherent blog content  
- Generate AI-based images using paragraph-level context  
- Maintain correct paragraph-to-image alignment  
- Web UI for input submission and result display  
- Option to regenerate:
  - Entire blog  
  - Individual paragraphs or images  

---

## Evaluation Criteria

- Relevance of content to topic and description  
- Semantic alignment between images and paragraphs  
- UI usability and clarity  
- End-to-end working flow  
- Code quality and modularity  

---

## Expected Outcome

A functional AI-powered blog generation web application that produces both text and images from a single blog description.

---

## System Architecture

### Frontend
- HTML5
- CSS3
- Responsive form-based UI
- Blog preview rendering

### Backend
- Python Flask application
- Handles blog content and image generation
- Uses Jinja templates for dynamic rendering

---

## Tech Stack

### Backend
- Python 3.x  
- Flask  
- Jinja2  

### Frontend
- HTML5  
- CSS3  

### Tooling
- Git and GitHub  
- Environment variables (`.env`)  

---

## Project Structure
```
AI-BLOG-GENERATOR/
│
├── templates/
│   └── index.html        # Main UI and blog preview template
│
├── app.py              # Flask backend entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── .gitignore

```

---

## How the Application Works

1. User opens the web application.
2. Enters the blog topic and description.
3. Selects target audience, tone, and blog length.
4. Optionally adds keywords.
5. Clicks **Generate Blog**.
6. Backend generates structured blog text and AI-generated images.
7. Each paragraph is displayed with its corresponding image.
8. Blog is previewed on the same page.

---

## Quick Start (Local Development)

### Prerequisites

- Python 3.9+
- pip
- Modern web browser

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-blog-generator-agent.git
cd ai-blog-generator-agent

```
### Step 2: Install Dependencies

```bash
pip install flask python-dotenv
```
### Step 3: Configure Environment Variables

Create a .env file in the root directory:
FLASK_ENV=development
FLASK_DEBUG=True

Add AI API keys here if required

### Step 4: Run the Application
python app.py
The application will be available at:
http://127.0.0.1:5000

### Edge Cases and Limitations
## Positive Cases
- Short and medium blog inputs generate results quickly

- Paragraph–image alignment is preserved

- UI works well on desktop browsers

### Limitations
- Very long blogs may increase generation time

- Image quality depends on the AI image model

- Export format may be limited initially

- Requires internet access if external AI services are used

## Future Requirements

- Include AI-generated images aligned with each blog paragraph  

- Ensure semantic matching between paragraph content and images  

- Support regeneration of individual images  

- Improve image quality and resolution  

- Add support for exporting blogs with embedded images (HTML / PDF)  


### Contributing

Contributions are welcome.

You may:

    - Submit pull requests for improvements or features

    - Open issues for bugs or suggestions

    - Improve UI, performance, or documentation

Please ensure contributions follow the existing project structure.

### Authors
Swayampakam Sathvika Bramhani

Kankanala Harshitha Reddy

Under the guidance and support of Coriolis 


### License

This project is licensed under the **MIT License**.
See the LICENSE file for details.

### Acknowledgments

- Flask open-source community

- AI text and image generation research community

- Hackathon organizers and mentors

- Open web standards (HTML & CSS)




