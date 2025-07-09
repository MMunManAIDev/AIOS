import argparse
import logging
from typing import Optional

import requests


class SCLI:
    """Simple semantic CLI that communicates with an LLMCore backend."""

    def __init__(self, model: str = "llama3", endpoint: str = "http://localhost:11434/api/generate") -> None:
        self.model = model
        self.endpoint = endpoint
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s: %(message)s",
        )

    def send_prompt(self, prompt: str) -> str:
        """Send a prompt to the backend and return the response."""
        payload = {"model": self.model, "prompt": prompt}
        try:
            resp = requests.post(self.endpoint, json=payload, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "")
        except Exception as exc:
            logging.error("Request failed: %s", exc)
            return f"Error: {exc}"

    def loop(self) -> None:
        """Interactively read user input and print LLM responses."""
        logging.info("Starting SCLI with model '%s'", self.model)
        while True:
            try:
                prompt = input("scli> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if not prompt:
                continue
            if prompt.lower() in {"exit", "quit"}:
                break

            result = self.send_prompt(prompt)
            print(result)
        logging.info("Exiting SCLI.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic CLI front end for LLMCore")
    parser.add_argument("--model", default="llama3", help="Model name to use")
    parser.add_argument(
        "--endpoint",
        default="http://localhost:11434/api/generate",
        help="LLMCore HTTP endpoint",
    )
    args = parser.parse_args()

    cli = SCLI(model=args.model, endpoint=args.endpoint)
    cli.loop()


if __name__ == "__main__":
    main()
