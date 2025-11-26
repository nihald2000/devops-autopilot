# Blaxel Setup Guide for Windows

## Prerequisites
- Windows 10/11
- Python 3.10+ installed
- PowerShell or Command Prompt

---

## Step 1: Install Blaxel CLI

### Option A: Using WSL (Recommended)

If you have WSL (Windows Subsystem for Linux) installed:

```bash
# In WSL terminal
curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=/usr/local/bin sudo -E sh
```

### Option B: Direct Download (Windows)

1. Download the Blaxel CLI from: https://github.com/blaxel-ai/toolkit/releases
2. Extract to `C:\Program Files\Blaxel\`
3. Add to PATH in System Environment Variables

### Option C: Skip CLI (Use SDK Only)

For development, you can use just the Python SDK without the CLI.

---

## Step 2: Login to Blaxel

### If using CLI:
```bash
bl login nihal
```

### If using SDK only:
Set environment variables in `.env`:
```env
BL_WORKSPACE=nihal
BL_API_KEY=your-api-key-here
```

Get your API key from: https://blaxel.ai/dashboard/settings/api-keys

---

## Step 3: Install Blaxel Python SDK ✅ DONE

```powershell
# In your project directory
cd C:\Users\HP\OneDrive\Desktop\agentic\dev\devops-autopilot

# Activate virtual environment
..\venv\Scripts\activate

# Install Blaxel SDK with all extras
pip install "blaxel[all]"
```

**Status**: ✅ Installing now...

---

## Step 4: Test SDK Installation

```powershell
python -c "from blaxel.core.sandbox import SandboxInstance; print('SDK installed!')"
```

**Expected output**: `SDK installed!`

---

## Step 5: Configure Environment Variables

Create or update `.env` file:

```env
# Blaxel Configuration
BL_WORKSPACE=nihal
BL_API_KEY=your-api-key-from-dashboard

# Optional: Model API Keys
OPENAI_API_KEY=your-openai-key
# ANTHROPIC_API_KEY=your-anthropic-key  # Not needed (no Claude)
```

**Get your keys from**:
- Blaxel: https://blaxel.ai/dashboard/settings/api-keys
- OpenAI: https://platform.openai.com/api-keys

---

## Step 6: Test Real Sandbox Creation

```python
import asyncio
from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration

async def test_sandbox():
    print("Creating sandbox...")
    config = SandboxCreateConfiguration(
        name="test-sandbox",
        image="blaxel/prod-base:latest"
    )
    sandbox = await SandboxInstance.create(sandbox=config)
    print(f"✅ Sandbox created: {sandbox.metadata.name}")
    
    # Clean up
    await sandbox.delete()
    print("✅ Sandbox deleted")

# Run test
asyncio.run(test_sandbox())
```

---

## Troubleshooting

### Import Error: `No module named 'blaxel'`
```powershell
# Make sure virtual environment is activated
..\venv\Scripts\activate

# Reinstall
pip install --upgrade "blaxel[all]"
```

### Authentication Error
```powershell
# Check environment variables
Get-Content .env

# Verify API key is set
echo $env:BL_API_KEY
```

### Sandbox Creation Fails
- Verify your Blaxel workspace has sandbox credits
- Check API key has correct permissions
- Ensure you're connected to internet

---

## Next Steps

Once setup is complete:

1. ✅ Test the updated `terraform_validator` with real sandboxes
2. Update other MCP servers to use real Blaxel infrastructure
3. Test end-to-end workflows
4. Deploy to production

---

## Quick Reference

**Check Blaxel CLI version**:
```bash
bl version
```

**List workspaces**:
```bash
bl workspaces
```

**Check SDK version**:
```powershell
python -c "import blaxel; print(blaxel.__version__)"
```

**Run DevOps Autopilot**:
```powershell
python app.py
```

---

**Status**: Installing Blaxel SDK with all extras...
