from pyvis.network import Network
from collections import defaultdict
import math
import webbrowser
import re

MODE_LIMITS = {
    "cpu": 1200,
    "balanced": 3000,
    "large": 8000,
    "full": 50000
}


def render_graph(events, functions, static_edges, mode="cpu"):

    limit = MODE_LIMITS.get(mode, 1200)

    net = Network(
        height="100vh",
        width="100%",
        bgcolor="#000000",
        font_color="#ffffff",
        directed=True
    )

    call_counts = defaultdict(int)
    edges = defaultdict(int)
    error_nodes = set()
    execution_sequence = []

    for e in events:

        if e["type"] == "call":
            call_counts[e["function"]] += 1
            execution_sequence.append(e["function"])

            if e["caller"]:
                edges[(e["caller"], e["function"])] += 1

        if e["type"] == "error":
            error_nodes.add(e["function"])

    for src, dst in static_edges:
        edges[(src, dst)] += 1

    nodes_sorted = sorted(
        call_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:limit]

    nodes = set(n[0] for n in nodes_sorted)

    max_calls = max(call_counts.values()) if call_counts else 1

    function_index = {}

    for key, info in functions.items():
        fn = key.split(":")[-1]

        if fn not in function_index:
            function_index[fn] = info

    for func, count in nodes_sorted:

        size = 8 + math.log(count + 1) * 6

        if func in error_nodes:
            color = "#ff3333"

        elif count > max_calls * 0.25:
            color = "#ffd000"

        else:
            color = "#ffffff"

        label = func.split(":")[-1]

        snippet = "source unavailable"

        runtime_fn = func.split(":")[-1]

        if runtime_fn in function_index:

            info = function_index[runtime_fn]

            try:

                with open(info["file"], "r", errors="ignore") as f:
                    lines = f.read().split("\n")

                snippet = "\n".join(
                    lines[max(0, info["line"]-5):info["line"]+20]
                )

            except:
                pass

        net.add_node(
            func,
            label=label,
            size=size,
            color=color,
            title=snippet
        )

    for (src, dst), count in edges.items():

        if src not in nodes or dst not in nodes:
            continue

        if count < 2 and mode != "full":
            continue

        width = 1 + math.log(count + 1)

        net.add_edge(
            src,
            dst,
            value=width,
            color="rgba(255,255,255,0.12)"
        )

    net.set_options("""
{
 "interaction":{
  "hover":true,
  "zoomView":true,
  "dragView":true,
  "navigationButtons":false
 },
 "physics":{
  "barnesHut":{
   "gravitationalConstant":-15000,
   "centralGravity":0.18,
   "springLength":120
  },
  "stabilization":{
   "enabled":true,
   "iterations":80
  }
 }
}
""")

    net.write_html("execution_graph.html")

    fix_html("execution_graph.html", execution_sequence)

    webbrowser.open("execution_graph.html")


def fix_html(file, execution_sequence):

    with open(file) as f:
        html = f.read()

    html = re.sub(r'<div class="vis-loading">.*?</div>', '', html, flags=re.S)

    html = html.replace(
        "</head>",
        """
<link rel="stylesheet" href="https://unpkg.com/vis-network/styles/vis-network.min.css">
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
</head>
"""
    )

    overlay = f"""
<style>

body {{
background:black;
color:white;
font-family:monospace;
}}

#loader-screen {{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:black;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
z-index:9999;
}}

.loader-bar {{
width:500px;
height:6px;
background:white;
margin-bottom:12px;
}}

.legend {{
position:fixed;
top:20px;
right:20px;
background:black;
border:1px solid #444;
padding:12px;
}}

.legend span {{
display:inline-block;
width:12px;
height:12px;
margin-right:6px;
}}

#code {{
position:fixed;
bottom:20px;
right:20px;
width:420px;
height:260px;
background:black;
color:white;
overflow:auto;
border:1px solid #444;
padding:10px;
white-space:pre-wrap;
z-index:999;
}}

#controls {{
position:fixed;
bottom:20px;
left:20px;
display:flex;
gap:10px;
z-index:999;
}}

.button {{
background:black;
color:white;
border:1px solid white;
padding:6px 12px;
cursor:pointer;
}}

.button:hover {{
background:white;
color:black;
}}

</style>

<div id="loader-screen">
<div class="loader-bar"></div>
<div>Executing SYNAPSE...</div>
</div>

<div class="legend">
<b>SYNAPSE</b><br><br>
<span style="background:white"></span> function<br>
<span style="background:#ffd000"></span> hotspot<br>
<span style="background:#ff3333"></span> error<br>
</div>

<pre id="code">Click node to view code</pre>

<div id="controls">
<button class="button" onclick="startReplay()">Replay</button>
<button class="button" onclick="stopReplay()">Stop</button>
</div>

<script>

setTimeout(function(){{
document.getElementById("loader-screen").style.display="none";
}},700);

network.on("click",function(params){{

if(!params.nodes.length) return;

var id=params.nodes[0];

var node=network.body.data.nodes.get(id);

if(node && node.title){{
document.getElementById("code").textContent=node.title;
}}

network.focus(id,{{scale:2}});

}});

var EXEC={execution_sequence};

var replayTimer=null;

function startReplay(){{
let i=0;

replayTimer=setInterval(function(){{
if(i>=EXEC.length) return;

let node=EXEC[i];

network.selectNodes([node]);
network.focus(node,{{scale:1.6}});

i++;
}},120);
}}

function stopReplay(){{
clearInterval(replayTimer);
}}

</script>
"""

    html = html.replace("</body>", overlay + "</body>")

    with open(file, "w") as f:
        f.write(html)
