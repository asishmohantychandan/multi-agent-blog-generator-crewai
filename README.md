# 🚀 CrewAI Multi-Agent Blog Generator

![CrewAI Banner](https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80\&w=1400\&auto=format\&fit=crop)

> An AI-powered multi-agent content generation system built using CrewAI, OpenAI/Groq LLMs, and real-time web search.

---

# 📌 Overview

This project demonstrates how multiple AI agents can collaborate together to perform:

* Real-time web research
* Strategic content analysis
* Automated blog writing

The system uses a sequential multi-agent workflow where each AI agent has a specialized role.

The final output is a fully generated Markdown blog post ready for publishing on platforms like:

* Medium
* LinkedIn
* Hashnode
* Dev.to

---

# 🧠 Multi-Agent Workflow

![AI Workflow](https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80\&w=1400\&auto=format\&fit=crop)

The system contains three specialized AI agents:

## 🔍 Research Agent

Responsible for:

* Searching real-time information
* Finding latest trends and statistics
* Gathering expert opinions
* Using Serper API for web search

---

## 📊 Analyst Agent

Responsible for:

* Extracting key insights
* Identifying patterns
* Structuring research findings
* Creating strategic narratives

---

## ✍️ Writer Agent

Responsible for:

* Writing engaging blog posts
* Simplifying complex topics
* Formatting content using Markdown
* Generating publish-ready articles

---

# ⚡ Features

✅ Multi-agent AI architecture using CrewAI
✅ Real-time web research with Serper API
✅ OpenAI and Groq LLM support
✅ Automated blog generation
✅ Modular agent-based design
✅ Environment variable validation
✅ Error handling and retries
✅ Markdown blog export
✅ Sequential AI workflow orchestration

---

# 🛠️ Tech Stack

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python             | Core programming language       |
| CrewAI             | Multi-agent orchestration       |
| OpenAI GPT-4o-mini | LLM support                     |
| Groq Llama 3.3     | Alternative LLM provider        |
| Serper API         | Real-time web search            |
| dotenv             | Environment variable management |

---

# 📂 Project Structure

```bash
multi-agent-blog-generator-crewai/
│
├── crewai_day1_final.py
├── requirements.txt
├── .env
├── .gitignore
├── blog_post.md
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/asishmohantychandan/multi-agent-blog-generator-crewai.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd multi-agent-blog-generator-crewai
```

---

## 3️⃣ Create Virtual Environment

### Using Conda

```bash
conda create -p venv python=3.10
```

Activate environment:

```bash
conda activate venv/
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

> You need at least one LLM API key:
>
> * OpenAI
> * Groq

---

# ▶️ Run the Project

```bash
python crewai_day1_final.py
```

---

# 📝 Example Output

The system automatically generates:

* Research insights
* Strategic analysis
* Complete blog article

Output file:

```bash
blog_post.md
```

---

# 📸 Sample Use Case

![AI Content Generation](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80\&w=1400\&auto=format\&fit=crop)

Example topic:

```python
result = crew.kickoff(inputs={"topic": "AI Agents in Healthcare 2026"})
```

Generated content includes:

* Industry trends
* Real-world examples
* Insights and analysis
* Conclusion with CTA

---

# 🔄 Workflow Execution

```text
Research Agent
      ↓
Analysis Agent
      ↓
Writer Agent
      ↓
Generated Blog Post
```

---

# 🧩 Key Concepts Demonstrated

This project demonstrates:

* AI Agents
* Multi-Agent Systems
* LLM Integration
* Prompt Engineering
* AI Workflow Automation
* Real-Time Data Retrieval
* Autonomous Content Generation
* Sequential Task Orchestration

---

# 🚧 Future Improvements

Planned enhancements:

* Streamlit frontend
* Blog export to PDF
* Automatic image generation
* Multi-language blog generation
* Agent memory support
* RAG integration
* Database support
* Deployment on cloud platforms

---

# 🌟 Why This Project Matters

This project showcases how autonomous AI systems can collaborate together to automate complex workflows.

It reflects practical applications of:

* Generative AI
* AI agents
* LLM orchestration
* Automated research systems

Such architectures are increasingly being used in:

* AI assistants
* Autonomous workflows
* Enterprise automation
* AI-powered SaaS products

---

# 🤝 Contributing

Contributions are welcome.

Feel free to:

* Fork the repository
* Open issues
* Suggest improvements
* Submit pull requests

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

## Asish Mohanty

Passionate about:

* Artificial Intelligence
* Machine Learning
* AI Agents
* Data Science
* Generative AI

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share it with others

---

# 🔗 Connect With Me

* LinkedIn: https://www.linkedin.com/in/asish-mohanty44
* GitHub: https://github.com/asishmohantychandan
* Medium: https://medium.com/@asishmohantychandan

---

> "The future belongs to intelligent autonomous systems powered by AI agents." 🚀
