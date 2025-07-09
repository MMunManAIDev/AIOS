# run_llm_core.py
from llm_core.service import LLMCoreService

if __name__ == "__main__":
    service = LLMCoreService()
    print("Type a prompt and press Enter (type 'exit' to quit)")
    while True:
        user_input = input("🧠> ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = service.handle_prompt(user_input)
        print(f"🤖 {response}")
