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
            "gpt-5": 0.005,  # Latest GPT-5 (Aug 2025)
            "gpt-4o": 0.0025,
            "gpt-4o-mini": 0.00015,
            "nebius/gpt-oss-120b": 0.0012,  # Nebius AI open-weight model
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
        # Routing logic based on task and complexity (OpenAI + Nebius only)
        routing_map = {
            ("terraform", TaskComplexity.COMPLEX): "gpt-5",  # GPT-5 best for complex reasoning
            ("terraform", TaskComplexity.MODERATE): "gpt-4o",
            ("terraform", TaskComplexity.SIMPLE): "gpt-4o-mini",
            
            ("security", TaskComplexity.COMPLEX): "gpt-5",  # Advanced security analysis
            ("security", TaskComplexity.MODERATE): "gpt-4o-mini",
            ("security", TaskComplexity.SIMPLE): "gpt-4o-mini",
            
            ("docker", TaskComplexity.COMPLEX): "gpt-5",
            ("docker", TaskComplexity.MODERATE): "nebius/gpt-oss-120b",  # Open-weight alternative
            ("docker", TaskComplexity.SIMPLE): "gpt-4o-mini",
            
            ("k8s", TaskComplexity.COMPLEX): "gpt-5",
            ("k8s", TaskComplexity.MODERATE): "gpt-4o",
            ("k8s", TaskComplexity.SIMPLE): "gpt-4o-mini",
            
            ("diff", TaskComplexity.COMPLEX): "nebius/gpt-oss-120b",  # Cost-effective for large diffs
            ("diff", TaskComplexity.MODERATE): "gpt-4o-mini",
            ("diff", TaskComplexity.SIMPLE): "gpt-4o-mini",
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
            "gpt-5": "Latest GPT-5 with enhanced reasoning and multimodal capabilities",
            "gpt-4o": "Balanced performance for general DevOps tasks",
            "gpt-4o-mini": "Fast & cost-effective for simple validations",
            "nebius/gpt-oss-120b": "Open-weight 120B model for cost-effective reasoning"
        }
        
        return f"""
**Model Selected**: {model}  
**Reason**: {explanations.get(model, 'Optimal for this task')}  
**Estimated Cost**: ${cost:.6f}  
**Task**: {task_type} ({complexity.value})
"""

# Global gateway instance
model_gateway = BlaxelModelGateway()
