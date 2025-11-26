from mcp.server.fastmcp import FastMCP
from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration
import time
import os

# Initialize MCP Server
mcp = FastMCP("terraform-validator")

@mcp.tool()
async def validate_terraform_plan(tf_code: str) -> str:
    """
    Validates Terraform code by running 'terraform plan' in a REAL Blaxel Sandbox.
    """
    print("=== REAL TERRAFORM VALIDATION STARTING ===")
    start_time = time.time()
    
    try:
        # STEP 1: Create REAL Blaxel sandbox
        print("Creating Blaxel sandbox...")
        config = SandboxCreateConfiguration(
            name=f"tf-val-{int(time.time())}",
            image="blaxel/base-image:latest",  # Terraform pre-installed
            memory=2048
        )
        sandbox = await SandboxInstance.create(sandbox=config)
        boot_time = (time.time() - start_time) * 1000
        print(f"[OK] Sandbox ready in {boot_time:.2f}ms")
        
        # STEP 2: Write Terraform code to sandbox
        print("Writing Terraform code to sandbox...")
        await sandbox.files.write("/workspace/main.tf", tf_code)
        
        # STEP 3: Initialize Terraform
        print("Running terraform init...")
        init_result = await sandbox.processes.exec(
            "cd /workspace && terraform init",
            timeout=30
        )
        
        if init_result.exit_code != 0:
            return f"ERROR: Terraform init failed\n{init_result.stderr}"
        
        # STEP 4: Run terraform plan
        print("Running terraform plan...")
        plan_result = await sandbox.processes.exec(
            "cd /workspace && terraform plan",
            timeout=60
        )
        
        # STEP 5: Format output
        total_time = (time.time() - start_time) * 1000
        
        output = f"""
=== REAL TERRAFORM VALIDATION COMPLETE ===
Sandbox: {sandbox.name}
Sandbox Boot Time: {boot_time:.2f}ms
Total Time: {total_time:.2f}ms

Terraform Plan Output:
{plan_result.stdout}

Exit Code: {plan_result.exit_code}
Status: {"[OK] SUCCESS" if plan_result.exit_code == 0 else "[FAIL]"}
"""
        
        # STEP 6: Clean up
        print("Cleaning up sandbox...")
        await sandbox.delete()
        
        return output
        
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    mcp.run()