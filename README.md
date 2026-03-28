# 🛠️ BuildRight: The Standalone Engineering Health Layer

**BuildRight** is a specialized FastMemory cognitive layer designed to ensure every line of code generated or reviewed by AI follows strict industry standards. 

## 🧠 Core Principles Included

- **Security (OWASP Top 10)**: Real-time identification of injection and data exposure patterns.
- **Architecture (SOLID)**: Architectural enforcement of decoupling and dependency inversion.
- **Code Hygiene**: Standardized naming, DRY compliance, and functional simplicity.

## 🚀 How to Use BuildRight

This project generates an Action-Topology Format (ATF) file that can be ingested by the [FastMemory](https://github.com/FastBuilderAI/memory) engine.

### 1. Generate the Memory
Run the generation script to create the latest `buildright.md`:
```bash
python3 generate.py
```

### 2. Ingest into FastMemory
You can now use this memory in your AI loops or IDE configurations:
```bash
# Build the BuildRight ontological graph
fastmemory build buildright.md

# Query the principles directly
fastmemory query buildright.md "injection"
```

### 3. Visualize the Memory
Open **`index.html`** directly in any modern web browser to view the interactive D3.js force-directed graph of the engineering health clusters.

## 🔧 Customizing Principles
To add or modify principles, edit `generate.py` and rerun the script.
