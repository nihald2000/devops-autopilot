import os
import sys
from blaxel.agents import Agent
from blaxel.run import run_agent
from utils.blaxel_client import BlaxelClient

# Initialize Blaxel Client
bl_client = BlaxelClient()

def validate_infrastructure(plan_content: str) -> str:
    """
    Validates a Terraform plan using a Blaxel Sandbox.
    """
    # This is a placeholder for the actual MCP tool logic
    # In a real scenario, this would call the MCP server
    return f"Validating plan with content length: {len(plan_content)}"

def scan_codebase(repo_url: str, scan_types: list[str] = ["trivy", "bandit"]) -> str:
    """
    Scans a codebase for security vulnerabilities.
    """
    return f"Scanning {repo_url} with {scan_types}..."

# Define the Agent
agent = Agent(
    name="devops-autopilot",
    model="gpt-4o",
    system_prompt="""
    You are DevOps Autopilot. Your goal is to assist with DevOps tasks using Blaxel infrastructure.
    You have access to tools that run in isolated sandboxes.
    Always verify infrastructure changes before applying them.
    """,
    tools=[validate_infrastructure, scan_codebase], # Register tools here
)

if __name__ == "__main__":
    # Run the agent using Blaxel's runner
    run_agent(agent)
