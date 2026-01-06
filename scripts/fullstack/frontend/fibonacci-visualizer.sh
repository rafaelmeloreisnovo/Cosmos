#!/bin/bash
# COSMOS Frontend - Fibonacci Sequence Visualizer
# D3.js-based visualization of modified Fibonacci sequences

cat > fibonacci-visualizer.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COSMOS - Fibonacci Visualizer</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        h1 {
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        
        .subtitle {
            text-align: center;
            opacity: 0.8;
            margin-bottom: 30px;
        }
        
        .controls {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .control-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        input, button {
            padding: 8px 15px;
            border-radius: 5px;
            border: none;
            font-size: 1em;
        }
        
        button {
            background: #4CAF50;
            color: white;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #45a049;
        }
        
        #visualization {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .spiral-path {
            fill: none;
            stroke: #2196F3;
            stroke-width: 2;
        }
        
        .point {
            fill: #FF9800;
            stroke: #F57C00;
            stroke-width: 2;
        }
        
        .golden-ratio {
            stroke: #FFD700;
            stroke-width: 1;
            stroke-dasharray: 5,5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌀 COSMOS Fibonacci Visualizer</h1>
        <p class="subtitle">Rafael Melo Reis - Modified Fibonacci Sequence</p>
        
        <div class="controls">
            <div class="control-group">
                <label for="terms">Number of Terms:</label>
                <input type="number" id="terms" value="15" min="3" max="30">
            </div>
            <div class="control-group">
                <label for="modifier">Golden Ratio Modifier (φ):</label>
                <input type="number" id="modifier" value="1.618" step="0.01" min="1" max="2">
            </div>
            <div class="control-group">
                <label>&nbsp;</label>
                <button onclick="generateVisualization()">Generate Visualization</button>
            </div>
        </div>
        
        <div id="visualization"></div>
    </div>
    
    <script>
        function modifiedFibonacci(n, modifier) {
            if (n <= 0) return [];
            if (n === 1) return [0];
            if (n === 2) return [0, 1];
            
            const sequence = [0, 1];
            for (let i = 2; i < n; i++) {
                const next = sequence[i-1] + sequence[i-2] * modifier;
                sequence.push(next);
            }
            return sequence;
        }
        
        function generateVisualization() {
            const terms = parseInt(document.getElementById('terms').value);
            const modifier = parseFloat(document.getElementById('modifier').value);
            
            const sequence = modifiedFibonacci(terms, modifier);
            
            // Clear previous visualization
            d3.select("#visualization").html("");
            
            const width = 1000;
            const height = 600;
            const centerX = width / 2;
            const centerY = height / 2;
            
            const svg = d3.select("#visualization")
                .append("svg")
                .attr("width", width)
                .attr("height", height);
            
            // Create spiral coordinates
            const points = sequence.map((value, index) => {
                const angle = index * modifier * 0.5;
                const radius = Math.log(value + 1) * 30;
                return {
                    x: centerX + radius * Math.cos(angle),
                    y: centerY + radius * Math.sin(angle),
                    value: value,
                    index: index
                };
            });
            
            // Draw spiral path
            const line = d3.line()
                .x(d => d.x)
                .y(d => d.y)
                .curve(d3.curveCardinal);
            
            svg.append("path")
                .datum(points)
                .attr("class", "spiral-path")
                .attr("d", line);
            
            // Draw points
            svg.selectAll(".point")
                .data(points)
                .enter()
                .append("circle")
                .attr("class", "point")
                .attr("cx", d => d.x)
                .attr("cy", d => d.y)
                .attr("r", 5)
                .append("title")
                .text(d => `F(${d.index}) = ${d.value.toFixed(2)}`);
            
            // Add labels for first few points
            svg.selectAll(".label")
                .data(points.slice(0, Math.min(8, points.length)))
                .enter()
                .append("text")
                .attr("x", d => d.x + 10)
                .attr("y", d => d.y - 10)
                .attr("fill", "#333")
                .attr("font-size", "12px")
                .text(d => `F${d.index}`);
            
            // Add title
            svg.append("text")
                .attr("x", width / 2)
                .attr("y", 30)
                .attr("text-anchor", "middle")
                .attr("font-size", "18px")
                .attr("fill", "#333")
                .text(`Modified Fibonacci Spiral (φ = ${modifier})`);
        }
        
        // Generate initial visualization
        generateVisualization();
    </script>
</body>
</html>
EOF

echo "✓ Fibonacci visualizer created: fibonacci-visualizer.html"
echo "  Open in browser to use the interactive visualization"
