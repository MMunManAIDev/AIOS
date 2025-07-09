# 🧠 AIOS — Cognitive OS with Native LLM Integration

A Semantically-Driven Operating System

**Version:** 0.1 (Prototype)
**Status:** Experimental, under active development

---

## 🧭 What is Cognitive OS?

**Cognitive OS** is a minimal Linux-based operating system where a hot-swappable Large Language Model (LLM) serves as a native, semantic interface layer to the system.

Imagine saying:  
> “Computer, please install Steam.”  
And your system just… does it.

This project reimagines how users and applications interact with an operating system — through intent, not syntax.

---

## 🧱 Core Features

- 🔁 **Hot-swappable LLM core** with standardized model contracts
- 💬 **Natural Language CLI** (Semantic Command Interface / `scli`)
- 🧠 LLM agent that understands the file system, packages, and running processes
- 🔐 **Sandboxed & audited** command execution
- 🧩 Pluggable architecture for semantic service hooks

---

## 📦 Components

- `llm-core`: Daemon that interfaces with your LLM (Ollama, LM Studio, etc.)
- `scli`: Semantic command-line interface
- `llmctl`: Utility to manage LLM sessions and switch models
- `model-adapter-layer`: Abstraction for LLM APIs and prompt routing
- `perm-broker` (optional): Validates risky actions and handles user consent

---

## 🚀 Quick Start (Prototype in a VM)

### Requirements
- VirtualBox, VMware, or KVM
- Ubuntu Server 22.04 (recommended)
- 2 vCPU, 4GB RAM+
- Python 3, `build-essential`, `git`, `curl`
- [Ollama](https://ollama.com) or LM Studio installed

### Setup Steps

```
# 1. Install dependencies sudo apt update && sudo apt install build-essential git curl python3 -y
# 2. Clone this repo git clone https://github.com/&lt;your-name&gt;/cognitive-os.git cd cognitive-os
# 3. Install and run Ollama (or your model server) ollama run llama3:8b
# 4. Start the llm-core service sudo systemctl enable llm-core sudo systemctl start llm-core
# 5. Run the semantic shell ./scli
```

## ⚙️ Example Use Cases
- “Find and delete all log files older than 30 days.”
- “Install Nginx and configure it to serve /var/www/html.”
- “Summarize system logs from the last boot.”

## 🧪 Roadmap
- MVP for scli
- Safe execution with confirmation mode
- GUI semantic window manager
- Per-user LLM session handling
- Voice input with Whisper/Vosk

## 🔐 Security
- All command executions are sandboxed
- Actions are logged and auditable
- Permission broker (optional) for elevated actions
- Hot-swap memory isolation between LLMs

## 📄 License
GPL-3.0

## 🤝 Contributing
Ideas, prototypes, and contributions are welcome. This project is in the early phase of exploring the next generation of human-computer interaction.

---

> “The computer is no longer a tool. It’s a collaborator.”

—
**AIOS: Cognitive Operating System**
