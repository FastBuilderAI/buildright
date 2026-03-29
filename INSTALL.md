# 🛡️ BuildRight: One Skill to Rule 130+ Frameworks

This guide provides the exact configuration to integrate BuildRight into your AI agent environment (Claude Desktop, Cursor, etc.). 

By following these 2 steps, you replace hundreds of manual `.md` files with a single, autonomous ontological skill.

---

## 🛠️ Step 1: Install the BuildRight MCP Server

BuildRight communicates via the **Model Context Protocol (MCP)**. Ensure you have the dependencies installed:

```bash
cd buildright
pip install -r requirements.txt
```

---

## 🔌 Step 2: Configure Your AI Desktop App

### 1. Claude Desktop (Mac)
Open your `claude_desktop_config.json`:
`~/Library/Application Support/Claude/claude_desktop_config.json`

Add the following to your `mcpServers` list:

```json
{
  "mcpServers": {
    "buildright": {
      "command": "python3",
      "args": [
        "/Users/prabhatsingh/FastBuilderAI-Sales/buildright/mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "/Users/prabhatsingh/FastBuilderAI-Sales/buildright"
      }
    }
  }
}
```

### 2. Cursor (IDE)
1. Go to **Settings > Features > MCP**.
2. Click **+ Add Server**.
3. Name: `BuildRight`
4. Type: `command`
5. Command: `python3 /Users/prabhatsingh/FastBuilderAI-Sales/buildright/mcp_server.py`

---

## 🧪 Step 3: Verify the "Horizontal Layer of Truth"

Once installed, restart your AI app and ask:

> "Query the BuildRight standards for **OWASP_A01** and ensure my current code follows the **CLEAN_CODE_SOLID** principles."

The AI will now pull the exact logic, data connections, and access controls from the 131-framework ontology in real-time.

---

## 💼 Enterprise Distribution
For high-scale mesh deployments or air-gapped sync, please refer to:
🔗 **[ENTERPRISE_PRICING.md](../memory/ENTERPRISE_PRICING.md)**
🛡️💻🧠
