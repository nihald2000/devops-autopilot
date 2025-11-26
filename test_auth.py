"""
Blaxel Authentication Test - Simple version
"""

import asyncio
import os
from dotenv import load_dotenv
from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration

load_dotenv()

async def test():
    print("=" * 60)
    print("TESTING BLAXEL AUTHENTICATION")
    print("=" * 60)
    
    workspace = os.getenv("BL_WORKSPACE")
    api_key = os.getenv("BL_API_KEY")
    
    print(f"Workspace: {workspace}")
    print(f"API Key: ***{api_key[-4:] if api_key else 'MISSING'}")
    print()
    
    try:
        print("Creating test sandbox...")
        config = SandboxCreateConfiguration(
            name="test-sandbox",
            image="blaxel/base-image:latest",
            memory=512
        )
        
        sandbox = await SandboxInstance.create(sandbox=config)
        print(f"[SUCCESS] Sandbox created: {sandbox.name}")
        
        print("Running test command...")
        result = await sandbox.processes.exec("echo 'Hello from Blaxel!'")
        print(f"[SUCCESS] Command output: {result.stdout.strip()}")
        
        print("Cleaning up...")
        await sandbox.delete()
        print("[SUCCESS] All tests passed!")
        
        print()
        print("=" * 60)
        print("[OK] BLAXEL IS WORKING!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test())
    exit(0 if success else 1)
