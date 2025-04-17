# 🧠 Research Agent

A lightweight, Python-powered research assistant agent that leverages custom tools and LLMs to automate and streamline knowledge discovery.

## 🚀 Features

- 🔌 Modular tool system via `tools.py`
- 🧠 LLM-powered research engine (OpenAI integration)
- 🧰 Easy to extend with new tools
- 🐍 Clean Python code, easy to understand and modify

## 📂 Project Structure

```
research-agent/
├── main.py           # Entry point for running the research agent
├── tools.py          # Collection of custom tools used by the agent
├── requirements.txt  # Python dependencies
└── .gitignore        # Ignored files for Git
```

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone git@github.com:IronClad1607/research-agent.git
   cd research-agent
   ```

2. **Start Virtual Environment**
```bash
source ./research-agent/bin/activate   
```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**
   Add your OpenAI key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the agent**
   ```bash
   python3 main.py
   ```

Then import and register it in `main.py`.

## 📌 Notes

- This project uses `dotenv` to manage API keys securely.
- Make sure you’re using Python 3.9+.

## 💡 Future Ideas

- Add memory for better multi-turn research
- Web scraping integration
- Support for multiple LLMs (Anthropic, Mistral, etc.)

## 👨‍💻 Author

Built by [IronClad1607](https://github.com/IronClad1607) — powered by curiosity and caffeine ☕.

---

Pull requests, issues, and stars are super welcome!
