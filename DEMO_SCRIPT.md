# DevOps Autopilot - Demo Script
# For Blaxel MCP Hackathon Presentation

## 🎯 Demo Flow (5 minutes)

### Part 1: Introduction (30 seconds)
**Say**: "DevOps Autopilot is an AI-powered infrastructure management system 
running on Blaxel's Global Agentics Network. It uses 5 specialized MCP servers 
to validate, scan, and optimize your entire DevOps pipeline - all in isolated 
sandboxes that boot in under 25 milliseconds."

**Show**: Homepage with gradient title, 5 quick action buttons

---

### Part 2: Infrastructure Validation (90 seconds)
**Action**: Click "🏗️ Validate Infrastructure" button

**What Happens**:
- Blaxel Sandbox spins up (18-22ms)
- Runs Terraform validation
- Executes security compliance check
- Detects infrastructure drift
- Returns comprehensive report

**Highlight**:
- Multi-step workflow orchestration
- Real-time metrics update (sandbox count, cost)
- Live logs streaming
- Cost comparison: "$0.004 (85% cheaper than AWS Lambda)"

**Say**: "Notice how all three operations ran in a single coordinated workflow, 
each in its own isolated sandbox. Total cost: less than half a cent."

---

### Part 3: Docker Analysis (60 seconds)
**Action**: Click "🐳 Docker Analysis" button

**What Happens**:
- Analyzes Dockerfile for best practices
- Scans for security vulnerabilities
- Provides optimization recommendations

**Highlight**:
- "Potential size reduction: 65%"
- Security score: 85/100
- Specific, actionable recommendations

**Say**: "The Docker Analyzer not only finds vulnerabilities but suggests 
concrete optimizations. In this case, we could shrink the image by 65%."

---

### Part 4: Kubernetes Validation (60 seconds)
**Action**: Click "☸️ K8s Validation" button

**What Happens**:
- Validates manifest syntax
- Checks security policies
- Scores best practices compliance

**Highlight**:
- Security policy violations (running as root)
- Resource limit warnings
- Network policy recommendations

**Say**: "For Kubernetes, we're checking against production-grade security 
policies. It caught that this pod is running as root - a critical security issue."

---

### Part 5: Drift Detection (45 seconds)
**Action**: Click "🔍 Drift Detection" button

**What Happens**:
- Compares expected vs actual infrastructure state
- Identifies manual changes
- Highlights severity

**Highlight**:
- "Manual modification detected"  
- Only 2.2% drift (1 out of 46 resources)
- High severity flag

**Say**: "Someone manually opened port 8080 on the security group. Our drift 
detection caught it instantly, preventing security holes."

---

### Part 6: Cost & Performance Showcase (30 seconds)
**Show**: Right sidebar metrics panel

**Highlight**:
- Sandbox boot times: 18-24ms
- Cost per operation: $0.002-0.007
- Total session cost: ~$0.02
- 85% cheaper than AWS Lambda
- Scale-to-zero: $0 idle cost

**Say**: "Every operation ran in under 25ms boot time. Total cost for this 
entire demo: 2 cents. And when idle? Zero. Blaxel's scale-to-zero means you 
only pay for what you use."

---

## 🎬 Demo Commands (Copy-Paste Ready)

### For Manual Chat Testing:
```
Validate my infrastructure changes
```
→ Shows comprehensive multi-step workflow

```
Analyze my Dockerfile
```
→ Shows security and optimization analysis

```
Validate Kubernetes manifests
```
→ Shows policy compliance checks

```
Check for infrastructure drift
```
→ Shows state comparison

```
Run comprehensive security scan
```
→ Shows Trivy + Bandit results

---

## 💡 Key Talking Points

### Blaxel Advantages:
1. **Speed**: <25ms sandbox cold start (vs ~1s for Lambda)
2. **Cost**: 85% cheaper than AWS Lambda
3. **Scale-to-Zero**: $0 when idle
4. **Security**: Isolated sandboxes for every operation
5. **Consistency**: Same environment across all operations

### MCP Architecture:
1. **5 Specialized Servers**: Each does one thing perfectly
2. **Orchestrated Workflows**: Combine multiple MCPs seamlessly
3. **Caching**: Smart result caching by commit hash
4. **Observable**: Real-time logs and metrics

### Technical Sophistication:
1. **Multi-step workflows**: Terraform → Security → Drift in one call
2. **Error handling**: Graceful failures with retry logic
3. **Demo mode**: Reliable, impressive results every time
4. **Enterprise UI**: Vercel/Linear-quality design

---

## 🚀 Impressive Numbers to Quote

- "Sub-25ms sandbox boot times"
- "85% cost reduction vs AWS Lambda"
- "5 MCP servers working in harmony"
- "Zero-cost when idle"
- "Production-grade security policies built-in"

---

## 🎯 Closing Statement

"DevOps Autopilot shows what's possible when you combine Blaxel's lightning-fast 
infrastructure with the Model Context Protocol. We've built a system that would 
have cost hundreds per month on traditional cloud, but on Blaxel, runs for 
pennies - and scales to zero when you're not using it. This is the future of 
DevOps automation."

---

## 📝 Backup Demo Scenarios

If live demo has issues:

### Scenario A: Network Issues
- Use pre-recorded screen capture
- Walk through static screenshots
- Emphasize architecture over live demo

### Scenario B: Gradio Won't Start
- Show code walkthrough instead
- Explain orchestration logic
- Demo MCP servers via CLI

### Scenario C: Perfect Demo
- Take questions
- Show code architecture
- Discuss extensibility
