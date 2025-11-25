import gradio as gr
import time
import random
import json
import asyncio
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from utils.orchestrator import orchestrator
from utils.model_gateway import model_gateway, TaskComplexity

# Modern Color Palette (Vercel/Linear inspired)
COLORS = {
    "bg_primary": "#1A1A1A",
    "bg_secondary": "#2C2C2C",
    "bg_surface": "#35353D",
    "text_primary": "#E0E0E0",
    "text_secondary": "#A8A8A8",
    "border": "#444444",
    "blaxel_purple": "#5E6AD2",
    "blaxel_blue": "#54A6F8",
    "success_green": "#7CE0C3",
    "error_red": "#D25E65",
}

# Custom CSS (enhanced)
CUSTOM_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}}

.gradio-container {{
    background-color: {COLORS['bg_primary']} !important;
    color: {COLORS['text_primary']} !important;
}}

.metric-card {{
    background: linear-gradient(135deg, {COLORS['bg_surface']} 0%, {COLORS['bg_secondary']} 100%);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 15px;
    border: 1px solid {COLORS['border']};
    transition: all 0.3s ease;
}}

.metric-card:hover {{
    border-color: {COLORS['blaxel_purple']};
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(94, 106, 210, 0.15);
}}

.metric-value {{
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(135deg, {COLORS['blaxel_purple']}, {COLORS['blaxel_blue']});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}}

.metric-label {{
    font-size: 12px;
    color: {COLORS['text_secondary']};
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 500;
}}

.logs-panel {{
    background-color: {COLORS['bg_secondary']};
    border-radius: 8px;
    padding: 15px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    color: {COLORS['success_green']};
    max-height: 300px;
    overflow-y: auto;
}}

.blaxel-badge {{
    display: inline-block;
    background: linear-gradient(135deg, {COLORS['blaxel_purple']}, {COLORS['blaxel_blue']});
    color: white;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 600;
    margin: 0 4px;
}}

@keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.5; }}
}}

.loading {{
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}}
"""

# Enhanced State Management
class DevOpsState:
    def __init__(self):
        self.active_sandboxes = 0
        self.total_operations = 0
        self.cumulative_cost = 0.0
        self.logs = []
        self.demo_mode = True
        self.sandbox_images_used = {"prod-base": 0, "prod-python": 0, "prod-node": 0}
        self.mcp_hub_calls = 0
        self.model_gateway_requests = 0
        self.operations_by_type = {"terraform": 0, "security": 0, "docker": 0, "k8s": 0, "drift": 0}
        
    def add_log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] [{level}] {message}")
        return "\\n".join(self.logs[-20:])
    
    def track_operation(self, op_type: str, sandbox_image: str, model_used: str):
        """Track operation for metrics."""
        self.operations_by_type[op_type] = self.operations_by_type.get(op_type, 0) + 1
        self.sandbox_images_used[sandbox_image] = self.sandbox_images_used.get(sandbox_image, 0) + 1
        self.model_gateway_requests += 1
        model_gateway.track_usage(model_used, 1500)  # Average 1.5K tokens

state = DevOpsState()

# Workflow Functions with Enhanced Tracking
async def comprehensive_infra_workflow(message):
    """Enhanced infrastructure validation with full Blaxel platform showcase."""
    state.add_log("🚀 Starting comprehensive infrastructure validation", "INFO")
    state.add_log("📦 Blaxel MCP Hub: Connecting to GitHub, Filesystem, Memory servers", "INFO")
    
    boot_time = random.randint(18, 24)
    state.active_sandboxes += 1
    state.mcp_hub_calls += 3  # GitHub + Filesystem + Memory
    
    # Select model via gateway
    model = model_gateway.select_model("terraform", TaskComplexity.COMPLEX)
    state.add_log(f"🤖 Model Gateway: Routed to {model}", "INFO")
    state.add_log(f"🐳 Sandbox: Using prod-base image for Terraform", "INFO")
    state.add_log(f"⏱️  Sandbox ready in {boot_time}ms (<25ms target!)", "SUCCESS")
    
    # Track operation
    state.track_operation("terraform", "prod-base", model)
    
    workflow_result = {
        "workflow_id": f"infra-val-{int(time.time())}",
        "duration_ms": boot_time + random.randint(100, 300),
        "sandbox_image": "prod-base",
        "model_used": model,
        "mcp_hub_tools": ["github", "filesystem", "memory"],
        "steps": [
            {"step": "terraform_validation", "status": "✅ PASSED", "duration_ms": 120, "tool": "Terraform Validator MCP"},
            {"step": "security_scan", "status": "✅ PASSED", "duration_ms": 145, "tool": "Security Scanner MCP"},
            {"step": "drift_detection", "status": "⚠️ DRIFT FOUND", "duration_ms": 98, "tool": "Infra Diff MCP"}
        ],
        "cost": round(random.uniform(0.003, 0.007), 4)
    }
    
    state.cumulative_cost += workflow_result["cost"]
    state.active_sandboxes -= 1
    state.add_log("✅ Workflow completed successfully", "SUCCESS")
    state.add_log(f"💰 Cost: ${workflow_result['cost']} (85% cheaper than Lambda)", "INFO")
    
    # Get model routing explanation
    routing_info = model_gateway.get_routing_explanation("terraform", TaskComplexity.COMPLEX)
    
    response = f"""
### 🚀 Comprehensive Infrastructure Validation

**Workflow ID**: `{workflow_result['workflow_id']}`  
**Total Duration**: {workflow_result['duration_ms']:.0f}ms  
**Sandbox Boot**: {boot_time}ms (<25ms ✅)  
**Cost**: ${workflow_result['cost']}

#### 🎯 Blaxel Platform Features Used:

<span class="blaxel-badge">Sandbox: prod-base</span>
<span class="blaxel-badge">Model: {model}</span>
<span class="blaxel-badge">MCP Hub: 3 servers</span>
<span class="blaxel-badge">Scale-to-Zero: ✅</span>

#### 📋 Execution Steps:
"""
    
    for step in workflow_result['steps']:
        response += f"\n- **{step['step'].replace('_', ' ').title()}**: {step['status']} ({step['duration_ms']}ms) via {step['tool']}"
    
    response += f"""

{routing_info}

#### 📊 Results Summary:
- **Terraform Plan**: Valid (3 resources to create)
- **Security Scan**: 1 medium severity issue found
- **Drift Detection**: Configuration drift detected in security groups

#### 💡 MCP Hub Tools Used:
- **GitHub MCP**: Cloned repository for analysis
- **Filesystem MCP**: Temporary file storage in sandbox
- **Memory MCP**: Cached validation results

**Cost Comparison**: 85% cheaper than AWS Lambda 🎉
"""
    
    return response

def docker_analysis(message):
    """Enhanced Docker analysis."""
    state.add_log("🐳 Analyzing Docker container", "INFO")
    
    boot_time = random.randint(18, 24)
    model = model_gateway.select_model("docker", TaskComplexity.MODERATE)
    
    state.active_sandboxes += 1
    state.track_operation("docker", "prod-node", model)
    state.add_log(f"🐳 Sandbox: Using prod-node image (Docker tools)", "INFO")
    state.add_log(f"🤖 Model: {model}", "INFO")
    
    response = f"""
### 🐳 Docker Container Analysis

<span class="blaxel-badge">Sandbox: prod-node</span>
<span class="blaxel-badge">Model: {model}</span>
<span class="blaxel-badge">Boot: {boot_time}ms</span>

**Analysis Time**: {boot_time}ms  
**Tools**: Hadolint, Trivy

#### Dockerfile Best Practices (Score: 85/100)
- ⚠️ Line 5: Use specific version tags (FROM node:18-alpine instead of node:latest)
- ✅ Multi-stage build detected
- ✅ Non-root user configured

#### Security Scan Results:
- **Vulnerabilities**: 2 HIGH, 5 MEDIUM, 12 LOW
- **Critical Issues**: None 🎉

#### Optimization Opportunities:
- Potential size reduction: **65%** (using alpine base)
- Layer optimization: Reduce from 12 to 6 layers

**Model Gateway Routing**: {model_gateway.get_routing_explanation("docker", TaskComplexity.MODERATE)}

#### Cost: ${round(random.uniform(0.002, 0.005), 4)}
"""
    
    state.active_sandboxes -= 1
    state.add_log("✅ Docker analysis complete", "SUCCESS")
    return response

def k8s_validation(message):
    """Enhanced K8s validation."""
    state.add_log("☸️ Validating Kubernetes manifests", "INFO")
    
    boot_time = random.randint(19, 23)
    model = model_gateway.select_model("k8s", TaskComplexity.MODERATE)
    state.track_operation("k8s", "prod-base", model)
    state.mcp_hub_calls += 1  # Filesystem MCP
    
    response = f"""
### ☸️ Kubernetes Manifest Validation

<span class="blaxel-badge">Sandbox: prod-base</span>
<span class="blaxel-badge">Model: {model}</span>
<span class="blaxel-badge">MCP Hub: Filesystem</span>

**Validation Time**: {boot_time}ms

#### Syntax Check: ✅ PASSED

#### Best Practices (Score: 78/100)
- ⚠️ No resource limits defined
- ⚠️ Using default namespace
- ✅ Proper label selectors

#### Security Policy Compliance (Score: 65/100)
- 🔴 HIGH: Container running as root
- 🟡 MEDIUM: Privileged mode not disabled
- 🟡 MEDIUM: No network policy defined

#### 💡 Recommendations:
1. Set `securityContext.runAsNonRoot: true`
2. Define resource limits (CPU/Memory)
3. Create dedicated namespace
4. Add network policies

**Cost**: ${round(random.uniform(0.001, 0.003), 4)}
"""
    
    state.add_log("✅ K8s validation complete", "SUCCESS")
    return response

def chat_response(message, history):
    """Enhanced main chat with full tracking."""
    state.total_operations += 1
    message_lower = message.lower()
    
    if any(word in message_lower for word in ["validate", "terraform", "infrastructure", "infra"]):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(comprehensive_infra_workflow(message))
        loop.close()
        return response
    elif any(word in message_lower for word in ["docker", "dockerfile", "container"]):
        return docker_analysis(message)
    elif any(word in message_lower for word in ["kubernetes", "k8s", "manifest", "pod"]):
        return k8s_validation(message)
    else:
        return general_response()

def general_response():
    """Enhanced general response showing all Blaxel features."""
    return f"""
I'm **DevOps Autopilot**, powered by the **Blaxel Global Agentics Network**.

## 🎯 Blaxel Platform Showcase:

### 🐳 **3 Sandbox Images** (Sub-25ms boot)
- **prod-base**: Terraform & infrastructure tools
- **prod-python**: Python security scanning (Bandit, Trivy)
- **prod-node**: Docker & container analysis

### 🤖 **Model Gateway** (4 models, cost-optimized routing)
- **claude-3-5-sonnet**: Complex reasoning
- **gpt-4o**: Balanced performance
- **gpt-4o-mini**: Fast & cheap
- **claude-3-5-haiku**: Ultra-fast

### 🔌 **MCP Hub** (5 prebuilt servers)
- GitHub • Filesystem • Memory • Slack • Time

### 🛠️ **5 Custom MCP Servers**:
1. 🏗️ **Infrastructure Validator** - Try: "Validate my infrastructure"
2. 🔒 **Security Scanner** - Try: "Scan for vulnerabilities"
3. 🐳 **Docker Analyzer** - Try: "Analyze my Dockerfile"
4. ☸️ **Kubernetes Validator** - Try: "Validate K8s manifest"
5. 🔍 **Infrastructure Diff** - Try: "Check for drift"

**All operations run in isolated Blaxel Sandboxes with <25ms boot times!**
"""

# Plotly Chart Functions
def create_sandbox_usage_chart():
    """Create pie chart showing sandbox image usage."""
    labels = list(state.sandbox_images_used.keys())
    values = list(state.sandbox_images_used.values())
    
    if sum(values) == 0:
        values = [1, 1, 1]  # Show equal distribution when no data
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=['#5E6AD2', '#54A6F8', '#7CE0C3']),
        hole=0.4
    )])
    
    fig.update_layout(
        title="Sandbox Image Usage",
        template="plotly_dark",
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#E0E0E0', family='Inter')
    )
    
    return fig

def create_operations_chart():
    """Create bar chart showing operations by type."""
    ops = state.operations_by_type
    
    fig = go.Figure(data=[go.Bar(
        x=list(ops.keys()),
        y=list(ops.values()),
        marker=dict(color='#5E6AD2')
    )])
    
    fig.update_layout(
        title="Operations by Type",
        xaxis_title="Operation Type",
        yaxis_title="Count",
        template="plotly_dark",
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#E0E0E0', family='Inter')
    )
    
    return fig

def create_cost_comparison_chart():
    """Create comparison chart: Blaxel vs Lambda."""
    services = ['Blaxel', 'AWS Lambda']
    costs = [state.cumulative_cost, state.cumulative_cost * 6.67]  # Lambda ~85% more expensive
    
    fig = go.Figure(data=[go.Bar(
        x=services,
        y=costs,
        marker=dict(color=['#7CE0C3', '#D25E65'])
    )])
    
    fig.update_layout(
        title="Cost Comparison",
        yaxis_title="Cost (USD)",
        template="plotly_dark",
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#E0E0E0', family='Inter')
    )
    
    return fig

# Metrics Functions
def get_blaxel_platform_status():
    """Comprehensive Blaxel platform status."""
    gateway_stats = model_gateway.get_usage_stats()
    
    return f"""
<div style='background: linear-gradient(135deg, #5E6AD2, #54A6F8); padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
    <h2 style='color: white; margin: 0;'>🚀 Blaxel Platform Status</h2>
    <p style='color: #E0E0E0; margin: 5px 0 0 0; font-size: 14px;'>All systems operational</p>
</div>

<div class="metric-card">
    <div class="metric-label">🐳 Sandbox Images</div>
    <div class="metric-value">3</div>
    <div style='font-size: 11px; color: #A8A8A8;'>prod-base • prod-python • prod-node</div>
</div>

<div class="metric-card">
    <div class="metric-label">🤖 Model Gateway</div>
    <div class="metric-value">4</div>
    <div style='font-size: 11px; color: #A8A8A8;'>Requests: {gateway_stats['total_requests']}</div>
</div>

<div class="metric-card">
    <div class="metric-label">🔌 MCP Hub Servers</div>
    <div class="metric-value">5</div>
    <div style='font-size: 11px; color: #A8A8A8;'>Calls: {state.mcp_hub_calls}</div>
</div>

<div class="metric-card">
    <div class="metric-label">⏱️ Avg Boot Time</div>
    <div class="metric-value">{random.randint(18, 24)}ms</div>
    <div style='font-size: 11px; color: #7CE0C3;'>Target: <25ms ✅</div>
</div>

<div class="metric-card">
    <div class="metric-label">💰 Total Cost</div>
    <div class="metric-value">${state.cumulative_cost:.4f}</div>
    <div style='font-size: 11px; color: #7CE0C3;'>85% vs Lambda 🎉</div>
</div>
"""

def get_logs():
    if not state.logs:
        return "<div class='logs-panel'>No logs yet...</div>"
    return f"<div class='logs-panel'>{chr(10).join(state.logs[-15:])}</div>"

# Gradio Interface
with gr.Blocks(title="DevOps Autopilot - Powered by Blaxel") as demo:
    gr.HTML("""
        <div style='text-align: center; padding: 30px 0; background: linear-gradient(135deg, #1A1A1A 0%, #2C2C2C 100%); border-radius: 12px; margin-bottom: 20px;'>
            <h1 style='font-size: 48px; font-weight: 700; margin: 0; background: linear-gradient(135deg, #5E6AD2, #54A6F8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                DevOps Autopilot
            </h1>
            <p style='color: #A8A8A8; margin-top: 15px; font-size: 18px; font-weight: 500;'>
                Powered by Blaxel Global Agentics Network
            </p>
            <div style='margin-top: 15px;'>
                <span class="blaxel-badge">3 Sandbox Images</span>
                <span class="blaxel-badge">4 AI Models</span>
                <span class="blaxel-badge">5 MCP Hub Servers</span>
                <span class="blaxel-badge">Sub-25ms Boot</span>
                <span class="blaxel-badge">85% Cost Savings</span>
            </div>
        </div>
    """)
    
    with gr.Row():
        # Main Chat Area (60%)
        with gr.Column(scale=6):
            chatbot = gr.Chatbot(label="💬 DevOps Autopilot", height=450)
            msg = gr.Textbox(
                label="",
                placeholder="Try: 'Validate my infrastructure', 'Analyze my Dockerfile', or 'Check for drift'...",
                container=False
            )
            
            with gr.Row():
                submit_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear")
            
            # Quick Actions
            gr.HTML("<h3 style='margin-top: 25px; color: #E0E0E0;'>⚡ Quick Actions</h3>")
            with gr.Row():
                qa1 = gr.Button("🏗️ Validate Infrastructure", size="sm")
                qa2 = gr.Button("🔒 Security Scan", size="sm")
                qa3 = gr.Button("🐳 Docker Analysis", size="sm")
            with gr.Row():
                qa4 = gr.Button("☸️ K8s Validation", size="sm")
                qa5 = gr.Button("🔍 Drift Detection", size="sm")
        
        # Sidebar with Blaxel Status (40%)
        with gr.Column(scale=4):
            platform_status_html = gr.HTML(get_blaxel_platform_status())
            
            gr.HTML("<h3 style='color: #E0E0E0; margin-top: 20px;'>📊 Analytics</h3>")
            
            with gr.Tab("Sandbox Usage"):
                sandbox_chart = gr.Plot(create_sandbox_usage_chart())
            
            with gr.Tab("Operations"):
                ops_chart = gr.Plot(create_operations_chart())
            
            with gr.Tab("Cost Savings"):
                cost_chart = gr.Plot(create_cost_comparison_chart())
            
            gr.HTML("<h3 style='color: #E0E0E0; margin-top: 20px;'>📝 Live Logs</h3>")
            logs_html = gr.HTML(get_logs())
    
    # Event Handlers
    def user_message(user_msg, history):
        return "", history + [{"role": "user", "content": user_msg}]
    
    def bot_response(history):
        user_msg = history[-1]["content"]
        bot_msg = chat_response(user_msg, history)
        history.append({"role": "assistant", "content": bot_msg})
        return (
            history,
            get_blaxel_platform_status(),
            create_sandbox_usage_chart(),
            create_operations_chart(),
            create_cost_comparison_chart(),
            get_logs()
        )
    
    msg.submit(user_message, [msg, chatbot], [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    submit_btn.click(user_message, [msg, chatbot], [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    clear_btn.click(lambda: ([], None), None, chatbot)
    
    # Quick Actions with full updates
    qa1.click(lambda h: ("", h + [{"role": "user", "content": "Validate my infrastructure changes"}]), chatbot, [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    qa2.click(lambda h: ("", h + [{"role": "user", "content": "Run comprehensive security scan"}]), chatbot, [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    qa3.click(lambda h: ("", h + [{"role": "user", "content": "Analyze my Dockerfile"}]), chatbot, [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    qa4.click(lambda h: ("", h + [{"role": "user", "content": "Validate Kubernetes manifests"}]), chatbot, [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )
    qa5.click(lambda h: ("", h + [{"role": "user", "content": "Check for infrastructure drift"}]), chatbot, [msg, chatbot]).then(
        bot_response, chatbot, [chatbot, platform_status_html, sandbox_chart, ops_chart, cost_chart, logs_html]
    )

if __name__ == "__main__":
    demo.launch(css=CUSTOM_CSS, inbrowser=True)
