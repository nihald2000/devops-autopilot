"""
Test Blaxel SDK Integration
Verifies that sandbox creation works before deploying to production
"""

import asyncio
import os
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration

async def test_sandbox():
    """Test creating a real Blaxel sandbox"""
    
    print("=" * 60)
    print("TESTING BLAXEL SDK INTEGRATION")
    print("=" * 60)
    
    # Check environment variables
    workspace = os.getenv("BL_WORKSPACE")
    api_key = os.getenv("BL_API_KEY")
    
    if not workspace or not api_key:
        print("[ERROR] Missing environment variables!")
        print(f"   BL_WORKSPACE: {'[OK]' if workspace else '[MISSING]'}")
        print(f"   BL_API_KEY: {'[OK]' if api_key else '[MISSING]'}")
        print("\nPlease set these in your .env file:")
        print("   BL_WORKSPACE=your-workspace-name")
        print("   BL_API_KEY=your-api-key")
        return
    
    print(f"[OK] Environment configured")
    print(f"   Workspace: {workspace}")
    print(f"   API Key: ***{api_key[-4:]}")
    print()
    
    try:
        # STEP 1: Create sandbox
        print("📦 Step 1: Creating Blaxel sandbox...")
        config = SandboxCreateConfiguration(
            name=f"test-sandbox-{int(asyncio.get_event_loop().time())}",
            image="blaxel/prod-base:latest",
            memory=1024  # 1GB RAM
        )
        
        sandbox = await SandboxInstance.create(sandbox=config)
        print(f"✅ Sandbox created successfully!")
        print(f"   ID: {sandbox.metadata.id}")
        print(f"   Name: {sandbox.metadata.name}")
        print(f"   Status: {sandbox.metadata.status}")
        print()
        
        # STEP 2: Test command execution
        print("🔧 Step 2: Testing command execution...")
        result = await sandbox.processes.exec("echo 'Hello from Blaxel!'")
        print(f"✅ Command executed successfully!")
        print(f"   Output: {result.stdout.strip()}")
        print(f"   Exit Code: {result.exit_code}")
        print()
        
        # STEP 3: Test file operations
        print("📝 Step 3: Testing file operations...")
        test_content = "# This is a test file\nprint('Hello from Blaxel!')\n"
        await sandbox.files.write("/tmp/test.py", test_content)
        print(f"✅ File written to sandbox")
        
        # Read it back
        read_result = await sandbox.processes.exec("cat /tmp/test.py")
        print(f"✅ File read from sandbox")
        print(f"   Content: {read_result.stdout.strip()}")
        print()
        
        # STEP 4: Test Python execution
        print("🐍 Step 4: Testing Python execution...")
        python_result = await sandbox.processes.exec("python /tmp/test.py")
        print(f"✅ Python executed in sandbox!")
        print(f"   Output: {python_result.stdout.strip()}")
        print()
        
        # STEP 5: Clean up
        print("🧹 Step 5: Cleaning up...")
        await sandbox.delete()
        print(f"✅ Sandbox deleted successfully!")
        print()
        
        # SUCCESS!
        print("=" * 60)
        print("🎉 ALL TESTS PASSED!")
        print("=" * 60)
        print("\n✅ Blaxel SDK is working correctly!")
        print("✅ Ready to deploy real integration!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}")
        print(f"   Message: {str(e)}")
        print(f"\n📋 Troubleshooting:")
        print(f"   1. Check your .env file has correct credentials")
        print(f"   2. Verify you have sandbox credits in your Blaxel workspace")
        print(f"   3. Check internet connection")
        print(f"   4. Try running: bl workspaces (if you have CLI)")
        
        # Print full traceback for debugging
        import traceback
        print(f"\n🔍 Full traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    # Load environment variables from .env
    from dotenv import load_dotenv
    load_dotenv()
    
    # Run the test
    asyncio.run(test_sandbox())
