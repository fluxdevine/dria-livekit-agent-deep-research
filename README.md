# 🧠 DRIA – Deep Research and Intelligence Agent
![logo](dria.png)
**A local-first voice assistant that multitasks like no other.**

---

### 🎙️ Talk to DRIA like a friend.  
While she silently conducts **deep research** in the background.

> Imagine asking your assistant to research a technical topic —  
> and casually switching to talk about lunch — without breaking flow.

---

## 🚀 What Makes DRIA Different?

Most assistants either:
- Go **silent** while they "think"
- Or give you **surface-level** responses fast

**DRIA does both.**
- 🧠 Performs **deep research** using Firecrawl (in a Docker container)
- 🔍 Uses **Perplexica** for quick, AI-powered local web searches
- 🗣️ Keeps chatting with you in real-time using **Mistral AI (3.1 small)** via Ollama
- 🎧 Fully **voice-enabled** via Faster-Whisper STT & Kokoro-82M TTS
- 🧩 Built on **LiveKit Voice Agent** + custom scripts
- 🔒 100% **local and private** – no data ever leaves your machine

---

## 🛠️ Tech Stack

| Feature              | Tool / Model                                                                 |
|----------------------|------------------------------------------------------------------------------|
| Voice Input          | [Faster-Whisper STT (Speaches AI)](https://github.com/speaches-ai/speaches)                      |
| Voice Output         | [Kokoro-82M  ](https://github.com/remsky/Kokoro-FastAPI)                                                 |
| LLM Engine           | [Mistral 3.1 small](https://mistral.ai/) (via Ollama)                        |
| Quick Web Search     | [Perplexica](https://github.com/ItzCrazyKns/Perplexica) – AI-powered local search engine |
| Deep Research Engine | [Firecrawl](https://firecrawl.dev/)                                          |
| Orchestration        | [LiveKit Agents](https://github.com/livekit/agents)                          |
| Containerized?       | ✅ Fully Dockerized                                                           |
| Cloud Calls?         | ❌ None – all local                                                           |

---

## 🧪 Capabilities

- 🔍 Quick Search for instant facts (via **Perplexica**)
- 🧠 Deep Research on complex topics (via **Firecrawl**)
- 💬 Real-time voice chat with natural conversation
- 📡 Parallel multitasking — keep talking while DRIA researches
- 🧾 Research history stored locally as JSON
- 🖼️ Photo editing and image generation via Stable Diffusion

---

## 📦 How to Run

> Instructions coming soon

---

## 🎧 DRIA's Personality

> “Helpful, intelligent, and totally unbothered by multitasking.”

Her tone is clear, warm, and professional — designed for smooth voice interactions.  
She explains what she's doing and lets you know when research is ready.

---

## 📁 File Highlights

- `dria-agent-deep-research.py.py` – DRIA’s brain and event loop
- `system_prompt.txt` – Defines her voice, behavior, and response rules
- `.env.local` – Place your configs (models, API ports, etc.)
- `tts.py` – Custom script for TTS
- `stt.py` – Custom script for STT

---

## 🖌️ Photo Editing Features

DRIA includes a local image model for quick edits and generative tweaks.

- **Upload an image** by saying "upload photo" and selecting a file when prompted.
- **Modify it** with natural language commands such as "brighten the colors" or "add a sunset".
- **Save or replace** the result once DRIA processes the request.

### Image Model Setup

1. Install `torch` and [`diffusers`](https://github.com/huggingface/diffusers).
2. Download a Stable Diffusion model into a `models/` folder.
3. Set `SD_MODEL_PATH` in `.env.local` to that folder so DRIA can load it at startup.

---

## 🤖 Powered by

- [Firecrawl](https://firecrawl.dev/)
- [Perplexica](https://github.com/ItzCrazyKns/Perplexica)
- [LiveKit Agents](https://github.com/livekit/agents)
- [Mistral](https://mistral.ai/)
- [Ollama](https://ollama.ai/)
- [Speaches AI](https://speaches.ai/)
- [Kokoro TTS](https://github.com/Kokoro-ai/tts)

---

## 💻 Local. Private. Yours.

> No cloud calls.  
> No data leaving your machine.  
> Just fast, intelligent research & conversation.

---

## 📍 Author

Built with ❤️ by [Dwain Barnes](https://github.com/dwain-barnes)  
Follow me on [LinkedIn](https://www.linkedin.com/in/dwain-barnes/) for updates & demos!

---


> _“Think deeply. Talk free. DRIA’s got you.”_
