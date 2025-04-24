# 🛠 Tool-Aware Agent (LangChain + OpenAI)

This project demonstrates how to build a LangChain agent that can use external tools as part of its reasoning process. This agent uses a calculator tool and performs reasoning with tools using `ReAct` strategy.

## 🧠 Agent Capabilities

- Understands natural language queries
- Breaks down problems using reasoning
- Uses tools like calculator to compute results
- Tracks token usage for every run

## 🧪 Example Query

```
User: What is 20% of the average of 3, 7, and 11?
→ Agent decides to use the calculator tool
→ Computes (3 + 7 + 11) / 3 = 7 → 7 * 0.2 = 1.4
→ Returns: 1.4
```

## 🛠 Tools Integrated

- 📐 `calculator_tool`: Evaluates basic Python expressions like percentages and averages

## 📁 Structure

```
module_6_tool_aware_agent/
├── main.py
├── tools/
│   └── calculator.py
├── utils/
│   └── token_counter.py
└── README.md
```

## 🚀 Run Instructions

```bash
pip install langchain langchain-openai langchain-community openai
export OPENAI_API_KEY="sk-..."
python main.py
```

## 📊 Token Usage

Tracked via `langchain_community.callbacks.manager.get_openai_callback()`.

---

MIT © Arun Annaldas
