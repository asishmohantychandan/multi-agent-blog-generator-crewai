# ── WARNINGS ───────────────────────────────────────────────
import warnings
warnings.filterwarnings("ignore")

# ── IMPORTS ────────────────────────────────────────────────
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# ── LOAD ENV ───────────────────────────────────────────────
load_dotenv()

# ── DEBUG ENV ──────────────────────────────────────────────
print("🔍 Checking environment variables...")
print("  SERPER_API_KEY :", "✅ FOUND" if os.getenv("SERPER_API_KEY") else "❌ MISSING")
print("  GROQ_API_KEY   :", "✅ FOUND" if os.getenv("GROQ_API_KEY")   else "❌ MISSING")
print("  OPENAI_API_KEY :", "✅ FOUND" if os.getenv("OPENAI_API_KEY") else "❌ MISSING")

# ── VALIDATION ─────────────────────────────────────────────
if not os.getenv("SERPER_API_KEY"):
    raise ValueError("❌ SERPER_API_KEY not found in .env")

# At least one LLM key must be present
if not os.getenv("GROQ_API_KEY") and not os.getenv("OPENAI_API_KEY"):
    raise ValueError("❌ Neither GROQ_API_KEY nor OPENAI_API_KEY found in .env — add at least one.")

# ── LLM CONFIG ─────────────────────────────────────────────
# Priority: if OPENAI_API_KEY is set, use GPT-4o-mini (fast + cheap).
# Falls back to Groq Llama if OpenAI key is missing.
# To switch manually, comment/uncomment the llm lines below.

from crewai import LLM

if os.getenv("OPENAI_API_KEY"):
    llm = LLM(
        model="gpt-4o-mini",
        temperature=0.5,     # balanced: factual but readable
        max_tokens=2000,     # enough for blog post sections
    )
    print("\n🤖 Using LLM: OpenAI gpt-4o-mini")
else:
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.5,
        max_tokens=2000,
    )
    print("\n🤖 Using LLM: Groq llama-3.3-70b-versatile")

# ── To force a specific provider, uncomment one of these: ──
# llm = "gpt-4o-mini"                      # OpenAI GPT-4o Mini
# llm = "gpt-4o"                           # OpenAI GPT-4o (more powerful)
# llm = "groq/llama-3.3-70b-versatile"     # Groq Llama 3.3 70B

# ── TOOL ───────────────────────────────────────────────────
search_tool = SerperDevTool()

# ── AGENTS ─────────────────────────────────────────────────
researcher = Agent(
    role="Tech Research Specialist",
    goal="Find accurate, comprehensive, and up-to-date information on {topic}",
    backstory=(
        "You are a senior researcher with 8+ years of experience tracking "
        "technology trends. You ALWAYS use tools for real-time data. "
        "If a tool fails, you clearly state: 'Real-time data unavailable'. "
        "You NEVER hallucinate or fabricate sources."
    ),
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=3,         # prevents infinite tool-call loops
    max_retry_limit=2,  # retries on failure before giving up
)

analyst = Agent(
    role="Strategic Content Analyst",
    goal="Extract the most valuable insights from research findings on {topic}",
    backstory=(
        "You are a strategic thinker who transforms raw research into clear "
        "narratives. You identify patterns others miss. "
        "If research data is weak or missing, you explicitly flag it."
    ),
    llm=llm,
    verbose=True,
    max_iter=3,
)

writer = Agent(
    role="Senior Content Writer",
    goal="Write clear, engaging, and well-structured blog posts on {topic}",
    backstory=(
        "You are a tech writer who makes complex ideas accessible. "
        "You write concise, high-quality blog content with a strong CTA. "
        "You NEVER repeat paragraphs and always avoid redundancy."
    ),
    llm=llm,
    verbose=True,
    max_iter=3,
)

# ── TASKS ──────────────────────────────────────────────────
research_task = Task(
    description=(
        "Research {topic} using the search tool. "
        "Find the latest trends, statistics, key players, and expert opinions "
        "from the past 12 months. "
        "If the search tool fails or returns no results, explicitly state: "
        "'Real-time data unavailable — proceeding with known information.'"
    ),
    expected_output=(
        "5-7 bullet points with real data, statistics, and sources about {topic}. "
        "OR a clear message explaining why data could not be retrieved."
    ),
    agent=researcher,
)

analysis_task = Task(
    description=(
        "Analyze the research findings on {topic}. "
        "Identify the top 3 most important insights for a general tech audience. "
        "Each insight must include: supporting data, a real-world example, "
        "and a note on confidence level if data was weak."
    ),
    expected_output=(
        "A structured outline with 3 key insights about {topic}, "
        "each containing: the insight, supporting evidence, and a real-world example."
    ),
    agent=analyst,
    context=[research_task],
)

writing_task = Task(
    description=(
        "Write a 600-800 word blog post about {topic} based on the analysis. "
        "Structure:\n"
        "  1. Engaging introduction (hook the reader)\n"
        "  2. Section 1 — First insight with explanation\n"
        "  3. Section 2 — Second insight with explanation\n"
        "  4. Section 3 — Third insight with explanation\n"
        "  5. Conclusion with a clear call to action\n"
        "Rules: No repeated paragraphs. Simple, clear language. "
        "Use Markdown headers (##) for sections."
    ),
    expected_output=(
        "A complete, ready-to-publish Markdown blog post with: "
        "title, introduction, 3 sections with ## headers, and a conclusion."
    ),
    agent=writer,
    context=[analysis_task],
    output_file="blog_post.md",
)

# ── CREW ───────────────────────────────────────────────────
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True,
    max_rpm=10,  # rate limit: max 10 requests/min to avoid API throttling
)

# ── RUN ────────────────────────────────────────────────────
print("\n🚀 Starting CrewAI Multi-Agent System...\n")

result = crew.kickoff(inputs={"topic": "AI Agents in Healthcare 2026"})

print("\n==========================================")
print("CREW FINISHED! Final Blog Post:")
print("==========================================\n")

# .raw gives clean string output 
print(result.raw)
print("\n📄 Blog post saved to: blog_post.md")