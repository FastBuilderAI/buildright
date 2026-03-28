import os
import json
import glob
import xml.etree.ElementTree as ET

try:
    import fastmemory
except ImportError:
    print("Error: 'fastmemory' library not found. Please install it with 'pip install fastmemory'.")
    exit(1)

# BuildRight: Universal Coding Health Layer for FastMemory
# This script generates an ATF (Action-Topology Format) file for FastMemory
# by dynamically loading framework definitions from the 'frameworks/' directory.

FRAMEWORKS_DIR = "frameworks"
PRINCIPLES = {}

def load_frameworks():
    """Load all JSON framework definitions from the frameworks directory."""
    global PRINCIPLES
    if not os.path.exists(FRAMEWORKS_DIR):
        print(f"Warning: Frameworks directory '{FRAMEWORKS_DIR}' not found.")
        return

    json_files = glob.glob(os.path.join(FRAMEWORKS_DIR, "*.json"))
    for file_path in json_files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                PRINCIPLES.update(data)
                print(f"Loaded JSON framework: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error loading JSON {file_path}: {e}")

    xml_files = glob.glob(os.path.join(FRAMEWORKS_DIR, "*.xml"))
    for file_path in xml_files:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            framework_name = root.attrib.get('name', os.path.basename(file_path))
            framework_rules = []
            for p in root.findall('principle'):
                rule = {
                    "id": p.attrib.get('id', 'UNKNOWN'),
                    "action": p.find('action').text if p.find('action') is not None else "",
                    "logic": p.find('logic').text if p.find('logic') is not None else "",
                    "data": p.find('data').text if p.find('data') is not None else "",
                    "access": p.find('access').text if p.find('access') is not None else "",
                    "event": p.find('event').text if p.find('event') is not None else ""
                }
                framework_rules.append(rule)
            PRINCIPLES[framework_name] = framework_rules
            print(f"Loaded XML framework: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error loading XML {file_path}: {e}")

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
        <h2>🛡️ BuildRight: Global Engineering Health Graph</h2>
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
                .text(d => d.isBlock ? d.name : d.id.split('_').slice(-1)[0]);

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
    
    # 0. Load External Frameworks
    load_frameworks()
    
    if not PRINCIPLES:
        print("Error: No principles loaded. Please check the 'frameworks/' directory.")
        return

    # 1. Generate core ATF text
    atf_content = generate_buildright_atf()
    with open(atf_file, "w") as f:
        f.write(atf_content)
    print(f"Successfully generated BuildRight ATF text ({len(atf_content)} chars) at: {atf_file}")

    # 2. Build Memory Graph
    print("Building Global Ontological Memory Graph using 'fastmemory' lib...")
    try:
        cbfdae_json_graph = fastmemory.process_markdown(atf_content)
        with open(json_file, "w") as f:
            f.write(cbfdae_json_graph)
        print(f"Successfully clustered unified memory graph into: {json_file}")
        
        # 3. Generate UI Data Bridge
        with open(js_file, "w") as f:
            f.write(f"const fastMemoryData = {cbfdae_json_graph};")
        print(f"Successfully generated UI bridge: {js_file}")

        # 4. Generate Interactive Dashboard
        with open(html_file, "w") as f:
            f.write(HTML_TEMPLATE)
        print(f"Successfully generated Global D3.js dashboard: {html_file}")
        
    except Exception as e:
        print(f"FastMemory engine error: {e}")

if __name__ == "__main__":
    main()
