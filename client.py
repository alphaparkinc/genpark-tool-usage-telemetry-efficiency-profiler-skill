"""
Agent Tool Usage Telemetry and Reliability Profiler.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional

class ToolTelemetryProfilerClient:
    """
    Profiles agent tool execution quality:
    - Success / failure rates per tool
    - Average execution duration
    - Reliability score based on error recurrence
    """

    def __init__(self):
        self.tool_stats = {} # tool_name -> {"invocations": int, "successes": int, "failures": int, "durations": []}

    def record_call(self, tool_name: str, duration_ms: float, success: bool, error_type: Optional[str] = None):
        """Records a tool invocation telemetry event."""
        if tool_name not in self.tool_stats:
            self.tool_stats[tool_name] = {
                "invocations": 0,
                "successes": 0,
                "failures": 0,
                "durations": [],
                "errors": {}
            }

        stats = self.tool_stats[tool_name]
        stats["invocations"] += 1
        if success:
            stats["successes"] += 1
        else:
            stats["failures"] += 1
            if error_type:
                stats["errors"][error_type] = stats["errors"].get(error_type, 0) + 1

        stats["durations"].append(duration_ms)
        if len(stats["durations"]) > 100:
            stats["durations"].pop(0)

    def get_tool_profile(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """Calculates reliability score and latency metrics for tool."""
        if tool_name not in self.tool_stats:
            return None

        stats = self.tool_stats[tool_name]
        inv = stats["invocations"]
        succ_rate = round((stats["successes"] / inv) * 100.0, 2) if inv > 0 else 0.0
        avg_lat = round(sum(stats["durations"]) / len(stats["durations"]), 2) if stats["durations"] else 0.0

        return {
            "tool_name": tool_name,
            "total_calls": inv,
            "success_rate_pct": succ_rate,
            "avg_latency_ms": avg_lat,
            "frequent_errors": stats["errors"],
            "reliability_tier": "HIGH" if succ_rate >= 90.0 else ("MEDIUM" if succ_rate >= 70.0 else "UNRELIABLE")
        }
