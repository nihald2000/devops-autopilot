import os
import time
from typing import Optional, Dict, Any
from blaxel.core.sandbox import SandboxInstance
from blaxel.core.sandbox.types import SandboxCreateConfiguration
from blaxel.core.agents import Agent
from blaxel.common import get_blaxel_client

class BlaxelClient:
    """
    Wrapper around Blaxel SDK to manage Sandboxes and Agent interactions.
    """
    def __init__(self):
        self.client = get_blaxel_client()
        self.workspace = os.getenv("BL_WORKSPACE")
        if not self.workspace:
            print("WARNING: BL_WORKSPACE not set. Some features may not work.")

    async def create_sandbox(self, name: str, image: str = "prod-base") -> SandboxInstance:
        """
        Creates a new Blaxel Sandbox instance.
        """
        print(f"Creating sandbox '{name}' with image '{image}'...")
        start_time = time.time()
        
        # Create sandbox instance using proper configuration
        config = SandboxCreateConfiguration(
            name=name,
            image=image
        )
        sandbox = await SandboxInstance.create(sandbox=config)
        
        boot_time = (time.time() - start_time) * 1000
        print(f"Sandbox '{name}' ready in {boot_time:.2f}ms")
        return sandbox

    def get_agent_config(self) -> Dict[str, Any]:
        """
        Returns the current agent configuration.
        """
        return {
            "model": "gpt-4o",
            "workspace": self.workspace
        }
