import logging
import os
from dotenv import load_dotenv
from .agents import (
    create_research_agent,
    create_source_checker_agent,
    create_scoring_agent,
)
from .memory import get_memory_base

load_dotenv()
logging.basicConfig(level=logging.INFO)


def run_ai_judge(question: str) -> str:
    print("\n" + "=" * 60)
    print("🤖 AI JUDGE — Internet Judge (LangChain 1.2.x)")
    print("=" * 60)
    print(f"📝 Question: {question}\n")

    # Agent 1
    print("🔍 Agent 1: Research...")
    research = create_research_agent()
    sub_q = research.invoke({"input": question})
    sub_questions = sub_q["output"]
    print(f"✅ {sub_questions}\n")

    # Agent 2
    print("🔍 Agent 2: Source Checker...")
    source = create_source_checker_agent()
    facts = source.invoke({"input": sub_questions})
    facts_and_sources = facts["output"]
    print(f"✅ {facts_and_sources}\n")

    # Agent 3
    print("🔍 Agent 3: Scoring...")
    memory = get_memory_base()
    scorer = create_scoring_agent(memory=memory)
    combined = f"Question: {question}\n\nFacts and sources:\n{facts_and_sources}"
    result = scorer.invoke({"input": combined})
    final_report = result["output"]
    print(f"✅ {final_report}\n")

    return final_report


def main():
    print("🧠 AI JUDGE — Internet Judge (LangChain)")
    print(f"📦 Model: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}")
    print("Type 'exit' to quit.\n")

    while True:
        q = input("❓ Ask: ")
        if q.lower() in ["exit", "quit"]:
            break
        if not q.strip():
            continue
        try:
            result = run_ai_judge(q)
            print("\n" + "=" * 60)
            print("📋 REPORT:")
            print("=" * 60)
            print(result)
            print("=" * 60 + "\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()
