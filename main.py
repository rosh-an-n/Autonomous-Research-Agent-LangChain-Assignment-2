"""Autonomous Research Agent — CLI Entry Point."""

import sys
from agent import research_topic
from report_generator import generate_report


def get_topic() -> str:
    """Get the research topic from command-line args or interactive input."""
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:]).strip()
        if topic:
            return topic

    print("=" * 60)
    print("  Autonomous Research Agent")
    print("  Powered by LangChain + OpenRouter")
    print("=" * 60)
    print()

    while True:
        topic = input("Enter a research topic (or 'quit' to exit): ").strip()
        if topic.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            sys.exit(0)
        if topic:
            return topic
        print("Please enter a valid topic.\n")


def main():
    """Main entry point for the research agent."""
    topic = get_topic()

    try:
        raw_output = research_topic(topic)
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error during research: {e}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print("  Generating Report...")
    print(f"{'='*60}\n")

    try:
        filepath = generate_report(topic, raw_output)
        print(f"Report saved to: {filepath}")
    except Exception as e:
        print(f"Error generating report: {e}")
        print("\nRaw research output:")
        print("-" * 40)
        print(raw_output)
        sys.exit(1)

    print(f"\n{'='*60}")
    print("  Research Complete!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
