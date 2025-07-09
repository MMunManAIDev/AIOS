import argparse
import logging
import sys
import requests


class LLMCoreService:
    """Basic runtime service for interacting with a local LLM."""

    def __init__(self, model: str = "llama3", base_url: str = "http://localhost:11434/api"):
        self.model = model
        self.base_url = base_url.rstrip("/")
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s: %(message)s",
        )

    def handle_prompt(self, prompt: str) -> str:
        """Send a prompt to the LLM and return its response."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(f"{self.base_url}/generate", json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "[No response in payload]")
        except requests.exceptions.ConnectionError:
            logging.error("LLM not available at %s", self.base_url)
            return "⚠️ LLM is offline. Is Ollama running?"
        except Exception as e:
            logging.exception("Failed to handle prompt")
            return f"❌ Error: {e}"


    def switch_model(self, model_name: str) -> None:
        """Switch the active model used for prompts."""
        logging.info("Switching model from %s to %s", self.model, model_name)
        self.model = model_name

    def run_loop(self) -> None:
        """Run a simple stdin loop for processing prompts."""
        logging.info("Starting LLMCoreService with model '%s'", self.model)
        for line in sys.stdin:
            prompt = line.strip()
            if not prompt:
                continue
            if prompt.lower() in {"exit", "quit"}:
                logging.info("Exiting LLMCoreService loop.")
                break
            response = self.handle_prompt(prompt)
            print(response, flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="LLM Core Service")
    parser.add_argument("--model", default="llama3", help="Model name to use")
    parser.add_argument(
        "--test", action="store_true", help="Run a single prompt then exit"
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:11434/api",
        help="Base URL for the LLM server",
    )
    args = parser.parse_args()

    service = LLMCoreService(model=args.model, base_url=args.base_url)

    if args.test:
        prompt = input("Prompt> ")
        print(service.handle_prompt(prompt))
    else:
        service.run_loop()


if __name__ == "__main__":
    main()
