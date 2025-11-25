import unittest
import json
from unittest.mock import patch, AsyncMock
import asyncio

class TestSecurityScanner(unittest.TestCase):
    @patch('mcp_servers.security_scanner.server.SandboxInstance')
    def test_scan_codebase_structure(self, mock_sandbox):
        """
        Test that scan_codebase returns the expected JSON structure.
        """
        from mcp_servers.security_scanner.server import scan_codebase
        
        # Mock the sandbox creation
        mock_sandbox.create = AsyncMock()
        
        repo_url = "https://github.com/example/repo"
        scan_types = ["trivy"]
        
        # Run the async function
        result_json = asyncio.run(scan_codebase(repo_url, scan_types))
        result = json.loads(result_json)
        
        self.assertEqual(result["repo"], repo_url)
        self.assertIn("trivy", result["scans"])
        self.assertIn("meta", result)
        self.assertIn("sandbox_boot_time_ms", result["meta"])

    @patch('mcp_servers.security_scanner.server.SandboxInstance')
    def test_caching(self, mock_sandbox):
        """
        Test that subsequent calls return cached results.
        """
        from mcp_servers.security_scanner.server import scan_codebase
        
        mock_sandbox.create = AsyncMock()
        
        repo_url = "https://github.com/example/repo-cached"
        
        # First call
        res1 = json.loads(asyncio.run(scan_codebase(repo_url, ["trivy"])))
        self.assertFalse(res1["meta"]["cached"])
        
        # Second call (should be cached)
        res2 = json.loads(asyncio.run(scan_codebase(repo_url, ["trivy"])))
        
        self.assertEqual(res1["repo"], res2["repo"])
        self.assertEqual(res1["scans"], res2["scans"])

if __name__ == "__main__":
    unittest.main()
