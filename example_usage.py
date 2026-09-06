"""
Demonstration of genpark-tool-usage-telemetry-efficiency-profiler-skill
"""

from client import ToolTelemetryProfilerClient

def main():
    profiler = ToolTelemetryProfilerClient()

    # Record 10 invocations for search tool
    for _ in range(9):
        profiler.record_call("web_search", duration_ms=120.0, success=True)
    profiler.record_call("web_search", duration_ms=450.0, success=False, error_type="RateLimitError")

    report = profiler.get_tool_profile("web_search")
    print("=== TOOL USAGE TELEMETRY REPORT ===")
    print("Tool Name:", report["tool_name"])
    print("Total Calls:", report["total_calls"])
    print("Success Rate:", f"{report['success_rate_pct']}%")
    print("Average Latency:", f"{report['avg_latency_ms']} ms")
    print("Reliability Tier:", report["reliability_tier"])

if __name__ == "__main__":
    main()
