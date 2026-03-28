import json
import os
from typing import Any, Dict, List, Optional
from mcp.server.fastapi import Context
from mcp.server import Server
import mcp.types as types
from mcp.server.stdio import stdio_server

# BuildRight: MCP Server for Claude Desktop
# Provides real-time engineering health checks by querying the FastMemory ontological graph.

GRAPH_PATH = "buildright.json"
MD_PATH = "buildright.md"

server = Server("buildright")

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available engineering health tools."""
    return [
        types.Tool(
            name="get_standards_overview",
            description="Get a high-level overview of the engineering standards currently loaded in BuildRight.",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        types.Tool(
            name="query_engineering_rule",
            description="Query the specific logic, data connections, and access controls for a coding principle.",
            inputSchema={
                "type": "object",
                "properties": {
                    "rule_id": {
                        "type": "string",
                        "description": "The unique ID of the rule to query (e.g., OWASP_A01, SOLID_SRP).",
                    }
                },
                "required": ["rule_id"],
            },
        ),
        types.Tool(
            name="search_best_practices",
            description="Search for engineering best practices by keyword (e.g., 'injection', 'decoupling').",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The keyword or topic to search for in the ontological memory.",
                    }
                },
                "required": ["query"],
            },
        )
    ]

def load_graph() -> List[Dict[str, Any]]:
    """Load the clustered buildright.json graph."""
    if not os.path.exists(GRAPH_PATH):
        return []
    with open(GRAPH_PATH, "r") as f:
        return json.load(f)

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: Dict[str, Any] | None
) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    if not arguments:
        arguments = {}

    graph = load_graph()
    
    if name == "get_standards_overview":
        frameworks = [block.get("name", "Unknown") for block in graph]
        return [types.TextContent(type="text", text=f"BuildRight currently enforces: {', '.join(frameworks)}")]

    elif name == "query_engineering_rule":
        rule_id = arguments.get("rule_id", "").upper()
        # Search for node in graph clusters
        for component in graph:
            for node in component.get("nodes", []):
                if node.get("id") == rule_id:
                    result = f"### [RULE: {rule_id}]\n"
                    result += f"**Action**: {node.get('action')}\n"
                    result += f"**Logic**: {node.get('logic', 'See buildright.md for full logic')}\n"
                    result += f"**Data Connection**: {node.get('data_connections')}\n"
                    return [types.TextContent(type="text", text=result)]
        return [types.TextContent(type="text", text=f"Error: Rule ID '{rule_id}' not found in the ontological memory.")]

    elif name == "search_best_practices":
        query = arguments.get("query", "").lower()
        matches = []
        for component in graph:
            for node in component.get("nodes", []):
                if query in node.get("id", "").lower() or query in node.get("action", "").lower():
                    matches.append(f"- {node.get('id')}: {node.get('action')}")
        
        if not matches:
            return [types.TextContent(type="text", text=f"No matches found for '{query}'.")]
        
        return [types.TextContent(type="text", text=f"Matches found:\n" + "\n".join(matches))]

    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
