"""
Blaxel Model Gateway Integration
Routes requests to optimal models based on task complexity and cost.
"""

from typing import Optional, Dict, Any
from enum import Enum

class TaskComplexity(Enum):
    """Task complexity levels for model selection."""
    SIMPLE = "simple"  # Fast, cheap models
    MODERATE = "moderate"  # Balanced models
    COMPLEX = "complex"  # Advanced reasoning models

class BlaxelModelGateway:
    """
    Routes requests through Blaxel's Model Gateway for cost-optimized AI operations.
    """
    
    def __init__(self):
        self.model_costs = {
            "gpt-4o-mini": 0.00015,  # per 1K tokens
            "gpt-4o": 0.0025,
            "claude-3-5-sonnet": 0.003,
            "claude-3-5-haiku": 0.0008,
        }
        
        self.total_cost = 0.0
        self.request_count = 0
        
    def select_model(self, task_type: str, complexity: TaskComplexity = TaskComplexity.MODERATE) -> str:
        """
        Intelligently select the best model for the task.
        
        Args:
            task_type: Type of task (terraform, security, docker, k8s, diff)
            complexity: Complexity level of the task
            
        Returns:
            Model name to use
        """
        # Routing logic based on task and complexity
        routing_map = {
            ("terraform", TaskComplexity.COMPLEX): "claude-3-5-sonnet",  # Best reasoning
            ("terraform", TaskComplexity.MODERATE): "gpt-4o",  # Good balance
            ("terraform", TaskComplexity.SIMPLE): "gpt-4o-mini",  # Fast & cheap
            
            ("security", TaskComplexity.COMPLEX): "gpt-4o",  # Security analysis
            ("security", TaskComplexity.MODERATE): "gpt-4o-mini",  # Quick scans
            ("security", TaskComplexity.SIMPLE): "claude-3-5-haiku",  # Fast checks
            
            ("docker", TaskComplexity.COMPLEX): "claude-3-5-sonnet",  # Optimization
            ("docker", TaskComplexity.MODERATE): "gpt-4o",  # Analysis
            ("docker", TaskComplexity.SIMPLE): "gpt-4o-mini",  # Quick checks
            
            ("k8s", TaskComplexity.COMPLEX): "claude-3-5-sonnet",  # Policy analysis
            ("k8s", TaskComplexity.MODERATE): "gpt-4o",  # Validation
            ("k8s", TaskComplexity.SIMPLE): "gpt-4o-mini",  # Syntax check
            
            ("diff", TaskComplexity.COMPLEX): "gpt-4o",  # State comparison
            ("diff", TaskComplexity.MODERATE): "gpt-4o-mini",  # Simple diff
            ("diff", TaskComplexity.SIMPLE): "claude-3-5-haiku",  # Quick check
        }
        
        model = routing_map.get((task_type, complexity), "gpt-4o-mini")
        
        return model
    
    def estimate_cost(self, model: str, estimated_tokens: int = 1000) -> float:
        """
        Estimate cost for a model call.
        
        Args:
            model: Model name
            estimated_tokens: Estimated token count
            
        Returns:
            Estimated cost in USD
        """
        cost_per_1k = self.model_costs.get(model, 0.001)
        return (estimated_tokens / 1000) * cost_per_1k
    
    def track_usage(self, model: str, tokens: int):
        """Track model usage and cost."""
        cost = self.estimate_cost(model, tokens)
        self.total_cost += cost
        self.request_count += 1
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics."""
        return {
            "total_requests": self.request_count,
            "total_cost": round(self.total_cost, 6),
            "avg_cost_per_request": round(self.total_cost / max(self.request_count, 1), 6),
            "cost_vs_lambda": round((1 - (self.total_cost / (self.request_count * 0.02))) * 100, 1) if self.request_count > 0 else 0
        }
    
    def get_routing_explanation(self, task_type: str, complexity: TaskComplexity) -> str:
        """
        Get human-readable explanation of model routing.
        """
        model = self.select_model(task_type, complexity)
        cost = self.estimate_cost(model)
        
        explanations = {
            "claude-3-5-sonnet": "Advanced reasoning for complex infrastructure analysis",
            "gpt-4o": "Balanced performance for general DevOps tasks",
            "gpt-4o-mini": "Fast & cost-effective for simple validations",
            "claude-3-5-haiku": "Ultra-fast for quick checks"
        }
        
        return f"""
**Model Selected**: {model}  
**Reason**: {explanations.get(model, 'Optimal for this task')}  
**Estimated Cost**: ${cost:.6f}  
**Task**: {task_type} ({complexity.value})
"""

# Global gateway instance
model_gateway = BlaxelModelGateway()
