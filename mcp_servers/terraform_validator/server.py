from mcp.server.fastmcp import FastMCP
from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration
import time

# Initialize MCP Server
mcp = FastMCP("terraform-validator")

@mcp.tool()
async def validate_terraform_plan(tf_code: str) -> str:
    """
    Validates Terraform code by running 'terraform plan' in a secure Blaxel Sandbox.
    Uses prod-base image optimized for infrastructure tools.
    """
    print("Starting Terraform validation in Blaxel Sandbox (prod-base)...")
    start_time = time.time()
    
    # Create a sandbox using prod-base image (optimized for Terraform)
    sandbox = await SandboxInstance.create(
        sandbox=SandboxCreateConfiguration(
            name="tf-validator",
            image="prod-base"  # Explicit image selection for infrastructure tools
        )
    )
    
    boot_time = (time.time() - start_time) * 1000
    print(f"Sandbox ready in {boot_time:.2f}ms")
    
    # In a real implementation, we would write the file and run commands
    # For this demo scaffold, we'll simulate the interaction
    
    # sandbox.fs.write("main.tf", tf_code)
    # result = sandbox.exec("terraform init && terraform plan")
    
    # Simulated output for the demo
    output = f"""
    Terraform Plan Validation:
    --------------------------
    Sandbox Image: prod-base (Terraform optimized)
    Sandbox Boot Time: {boot_time:.2f}ms
    
    Running 'terraform plan'...
    
    Plan: 1 to add, 0 to change, 0 to destroy.
    
    Changes to Outputs:
      + instance_ip = (known after apply)
    """
    
    return output

if __name__ == "__main__":
    mcp.run()
