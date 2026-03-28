import os
import json

try:
    import fastmemory
except ImportError:
    print("Error: 'fastmemory' library not found. Please install it with 'pip install fastmemory'.")
    exit(1)

# BuildRight: Universal Coding Health Layer for FastMemory
# This script generates an ATF (Action-Topology Format) file for FastMemory
# and processes it using the official fastmemory Python library.
# It also generates a D3.js force-directed graph for interactive visualization.

PRINCIPLES = {
    "Security_OWASP": [
        {
            "id": "OWASP_A1_INJECTION",
            "action": "Prevent_Injection",
            "logic": "Always use parameterized queries or prepared statements for database, LDAP, and OS command calls. Never concatenate unsanitized user input into executable strings.",
            "data": "[parameterized_queries], [sql_injection], [prepared_statements]",
            "access": "Role_Security_Auditor",
            "event": "On_Database_Query"
        },
        {
            "id": "OWASP_A2_BROKEN_AUTH",
            "action": "Secure_Authentication",
            "logic": "Implement secure session management, multi-factor authentication, and robust password hashing (e.g., Argon2, bcrypt). Protect against session hijacking and automated credential stuffing.",
            "data": "[session_token], [mfa], [password_hashing]",
            "access": "Role_Auth_Manager",
            "event": "On_User_Login"
        },
        {
            "id": "OWASP_A3_SENSITIVE_DATA",
            "action": "Protect_Data",
            "logic": "Encrypt sensitive data at rest using AES-256 and in transit using TLS 1.3. Avoid storing unnecessary PII and rotate encryption keys periodically.",
            "data": "[encryption_at_rest], [tls_1.3], [pii]",
            "access": "Role_Compliance_Officer",
            "event": "On_Data_Storage"
        }
    ],
    "Architecture_SOLID": [
        {
            "id": "SOLID_SRP",
            "action": "Enforce_SRP",
            "logic": "Single Responsibility Principle: A class or module should have one, and only one, reason to change. Decouple logic into specialized, focused components.",
            "data": "[module_decoupling], [focused_classes], [single_responsibility]",
            "access": "Role_Architect",
            "event": "On_Component_Design"
        },
        {
            "id": "SOLID_OCP",
            "action": "Enforce_OCP",
            "logic": "Open-Closed Principle: Software entities should be open for extension but closed for modification. Use interfaces and polymorphism to allow behavior changes without altering existing code.",
            "data": "[polymorphism], [interfaces], [extensions]",
            "access": "Role_Architect",
            "event": "On_Feature_Expansion"
        },
        {
            "id": "SOLID_DIP",
            "action": "Enforce_DIP",
            "logic": "Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions. Use dependency injection to manage lifecycle and mockability.",
            "data": "[dependency_injection], [abstractions], [mocking]",
            "access": "Role_Architect",
            "event": "On_Service_Initialization"
        }
    ],
    "Code_Hygiene": [
        {
            "id": "PRINCIPLE_DRY",
            "action": "Avoid_Repetition",
            "logic": "Don't Repeat Yourself: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system. Use abstractions to consolidate duplicated logic.",
            "data": "[code_reuse], [abstraction_layer], [authority_source]",
            "access": "Role_Developer",
            "event": "On_Code_Review"
        },
        {
            "id": "PRINCIPLE_KISS",
            "action": "Simplify_Logic",
            "logic": "Keep It Simple, Stupid: Most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided.",
            "data": "[simplicity], [minimalism], [no_overengineering]",
            "access": "Role_Developer",
            "event": "On_Logic_Implementation"
        },
        {
            "id": "PRINCIPLE_YAGNI",
            "action": "Defer_Features",
            "logic": "You Ain't Gonna Need It: Always implement things when you actually need them, never when you just foresee that you may need them. Avoid speculative generality.",
            "data": "[deferred_execution], [actual_requirements], [no_speculation]",
            "access": "Role_Developer",
            "event": "On_Project_Planning"
        }
    ],
    "Clean_Code": [
        {
            "id": "CLEAN_NAMES",
            "action": "Use_Meaningful_Names",
            "logic": "Variables, functions, and classes should have names that reveal intent. A name should tell you why it exists, what it does, and how it is used.",
            "data": "[intent_naming], [self_documenting], [readability]",
            "access": "Role_Developer",
            "event": "On_Variable_Declaration"
        },
        {
            "id": "CLEAN_FUNCTIONS",
            "action": "Keep_Functions_Small",
            "logic": "Functions should be small, should do only one thing, and should do it well. Large functions indicate high cyclomatic complexity and low maintainability.",
            "data": "[functional_purity], [cyclomatic_complexity], [small_scope]",
            "access": "Role_Developer",
            "event": "On_Function_Definition"
        }
    ]
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>BuildRight - Ontological Memory Visualization</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: -apple-system, sans-serif; margin: 0; padding: 20px; background: #0f172a; color: white; overflow: hidden; }
        .header { margin-bottom: 20px; border-bottom: 1px solid #1e293b; padding-bottom: 10px; }
        .header h2 { margin: 0; color: #3b82f6; }
        .header p { margin: 5px 0 0; color: #94a3b8; font-size: 14px; }
        .node { stroke: #fff; stroke-width: 1.5px; cursor: pointer; }
        .link { stroke: #334155; stroke-opacity: 0.6; }
        svg { background: #1e293b; border-radius: 12px; width: 100%; height: calc(100vh - 120px); }
        .label { font-size: 10px; fill: white; pointer-events: none; text-shadow: 0 1px 2px rgba(0,0,0,0.8); }
        .tooltip {
            position: absolute; text-align: left; padding: 12px; font-size: 12px;
            background: rgba(15, 23, 42, 0.95); color: #cbd5e1; border: 1px solid #334155; border-radius: 8px; 
            pointer-events: none; opacity: 0; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
            max-width: 320px; line-height: 1.4;
        }
        .legend { position: absolute; bottom: 40px; right: 40px; background: rgba(30, 41, 59, 0.8); padding: 15px; border-radius: 8px; border: 1px solid #334155; }
        .legend-item { display: flex; align-items: center; margin-bottom: 5px; font-size: 12px; }
        .legend-color { width: 12px; height: 12px; border-radius: 50%; margin-right: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <h2>🛡️ BuildRight: Engineering Health Graph</h2>
        <p>Interactive CBFDAE Ontological Memory clustered by FastMemory Louvain engine.</p>
    </div>
    
    <div id="chart"></div>
    <div id="tooltip" class="tooltip"></div>
    
    <div class="legend">
        <div class="legend-item"><div class="legend-color" style="background: #3b82f6;"></div> Block</div>
        <div class="legend-item"><div class="legend-color" style="background: #8b5cf6;"></div> Function</div>
        <div class="legend-item"><div class="legend-color" style="background: #eab308;"></div> Data</div>
        <div class="legend-item"><div class="legend-color" style="background: #22c55e;"></div> Access</div>
        <div class="legend-item"><div class="legend-color" style="background: #ef4444;"></div> Event</div>
    </div>

    <script src="buildright.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            if (typeof fastMemoryData === 'undefined') {
                document.getElementById('chart').innerHTML = "<p style='color:white; padding: 20px;'>Error: fastMemoryData not defined. Run generate.py first.</p>";
                return;
            }
            renderGraph();
        });
        
        function renderGraph() {
            const width = window.innerWidth - 40;
            const height = window.innerHeight - 120;
            
            const nodes = [];
            const links = [];
            const nodeMap = new Map();
            
            function flattenBlocks(blocks, parentBlock) {
                blocks.forEach((block, i) => {
                    const blockId = block.id;
                    if (!nodeMap.has(blockId)) {
                        nodes.push({ id: blockId, group: i+1, name: block.name, size: 25, isBlock: true, cbfdae: block.cbfdae_level || "Block", desc: "Clustered Principle Category" });
                        nodeMap.set(blockId, true);
                    }
                    
                    if (parentBlock) {
                        links.push({ source: parentBlock, target: blockId, value: 5, linkType: "hierarchy" });
                    }
                    
                    if (block.nodes && Array.isArray(block.nodes)) {
                        block.nodes.forEach(n => {
                            if(!nodeMap.has(n.id)) {
                                let n_color = "#3b82f6"; 
                                if (n.cbfdae_level === "Data") n_color = "#eab308";
                                if (n.cbfdae_level === "Access") n_color = "#22c55e";
                                if (n.cbfdae_level === "Event") n_color = "#ef4444";
                                if (n.cbfdae_level === "Function") n_color = "#8b5cf6";

                                nodes.push({ id: n.id, action: n.action, group: i+1, name: n.id, size: 8, isBlock: false, cbfdae: n.cbfdae_level || "Function", desc: "Logic: " + (n.logic||"none"), color: n_color });
                                nodeMap.set(n.id, true);
                            }
                            links.push({ source: n.id, target: blockId, value: 1, linkType: "hierarchy" });
                            
                            if (n.data_connections && Array.isArray(n.data_connections)) {
                                n.data_connections.forEach(target => {
                                    if(nodeMap.has(target)) links.push({ source: n.id, target: target, value: 0.2, linkType: "data" });
                                });
                            }
                        });
                    }
                    
                    if (block.sub_blocks && Array.isArray(block.sub_blocks)) {
                        flattenBlocks(block.sub_blocks, blockId);
                    }
                });
            }
            
            flattenBlocks(fastMemoryData, null);

            const sim = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => d.id).distance(80))
                .force("charge", d3.forceManyBody().strength(-150))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.1))
                .force("y", d3.forceY(height / 2).strength(0.1))
                .force("collide", d3.forceCollide().radius(d => d.size + 20));

            const svg = d3.select("#chart").append("svg")
                .attr("viewBox", [0, 0, width, height]);

            const link = svg.append("g")
                .selectAll("line")
                .data(links)
                .join("line")
                .attr("class", "link")
                .attr("stroke-width", d => d.linkType === 'hierarchy' ? 1.5 : 0.8)
                .attr("stroke", d => d.linkType === 'data' ? "#eab308" : d.linkType === 'access' ? "#22c55e" : d.linkType === 'event' ? "#ef4444" : "#334155")
                .attr("stroke-dasharray", d => d.linkType === 'hierarchy' ? "none" : "3,3");

            const colorScale = d3.scaleOrdinal(d3.schemeCategory10);
            const node = svg.append("g")
                .selectAll("circle")
                .data(nodes)
                .join("circle")
                .attr("class", "node")
                .attr("r", d => d.size)
                .attr("fill", d => d.isBlock ? colorScale(d.group) : d.color || "#3b82f6")
                .call(d3.drag()
                    .on("start", (event, d) => {
                        if (!event.active) sim.alphaTarget(0.3).restart();
                        d.fx = d.x; d.fy = d.y;
                    })
                    .on("drag", (event, d) => {
                        d.fx = event.x; d.fy = event.y;
                    })
                    .on("end", (event, d) => {
                        if (!event.active) sim.alphaTarget(0);
                        d.fx = null; d.fy = null;
                    }));

            const label = svg.append("g")
                .selectAll("text")
                .data(nodes)
                .join("text")
                .attr("class", "label")
                .attr("text-anchor", "middle")
                .text(d => d.isBlock ? d.name : d.id.replace('PRINCIPLE_', ''));

            const tooltip = d3.select("#tooltip");

            node.on("mouseover", (event, d) => {
                tooltip.transition().duration(200).style("opacity", .9);
                tooltip.html("<strong>" + d.id + "</strong><br/>" + d.desc)
                       .style("left", (event.pageX + 15) + "px")
                       .style("top", (event.pageY - 28) + "px");
            }).on("mouseout", () => {
                tooltip.transition().duration(500).style("opacity", 0);
            });

            sim.on("tick", () => {
                link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
                
                // Keep circles in bounds
                node.attr("cx", d => d.x = Math.max(d.size, Math.min(width - d.size, d.x)))
                    .attr("cy", d => d.y = Math.max(d.size, Math.min(height - d.size, d.y)));
                
                label.attr("x", d => d.x).attr("y", d => d.y + 4);
            });
        }
    </script>
</body>
</html>
"""

def generate_buildright_atf():
    atf_content = "# BuildRight: Universal Coding Health Layer\n\n"
    for category, rules in PRINCIPLES.items():
        atf_content += f"## {category.replace('_', ' ')}\n\n"
        for rule in rules:
            atf_content += f"### [ID: {rule['id']}]\n"
            atf_content += f"**Action:** {rule['action']}\n"
            atf_content += f"**Input:** {{Context}}\n"
            atf_content += f"**Logic:** {rule['logic']}\n"
            atf_content += f"**Data_Connections:** {rule['data']}\n"
            atf_content += f"**Access:** {rule['access']}\n"
            atf_content += f"**Events:** {rule['event']}\n\n"
    return atf_content

def main():
    atf_file = "buildright.md"
    json_file = "buildright.json"
    js_file = "buildright.js"
    html_file = "index.html"
    
    # 1. Generate core ATF text
    atf_content = generate_buildright_atf()
    with open(atf_file, "w") as f:
        f.write(atf_content)
    print(f"Successfully generated BuildRight ATF text at: {atf_file}")

    # 2. Build Memory Graph
    print("Building Ontological Memory Graph using 'fastmemory' lib...")
    try:
        cbfdae_json_graph = fastmemory.process_markdown(atf_content)
        with open(json_file, "w") as f:
            f.write(cbfdae_json_graph)
        print(f"Successfully clustered memory graph into: {json_file}")
        
        # 3. Generate UI Data Bridge
        with open(js_file, "w") as f:
            f.write(f"const fastMemoryData = {cbfdae_json_graph};")
        print(f"Successfully generated UI bridge: {js_file}")

        # 4. Generate Interactive Dashboard
        with open(html_file, "w") as f:
            f.write(HTML_TEMPLATE)
        print(f"Successfully generated D3.js dashboard: {html_file}")
        
    except Exception as e:
        print(f"FastMemory engine error: {e}")

if __name__ == "__main__":
    main()
