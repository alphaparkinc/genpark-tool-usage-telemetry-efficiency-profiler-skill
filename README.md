# GenPark AI Agent Skill - Tool Telemetry Profiler

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Tool usage telemetry accumulator measuring success ratios, failure modes, and execution latency.

```mermaid
flowchart TD
    A[Tool Invocations] --> B[Telemetry Collector]
    B --> C[Success Rate Calculator]
    B --> D[Latency Moving Average]
    B --> E[Error Recurrence Classifier]
    C & D & E --> F[Tool Reliability Tier Score]
```

## Features
- **Reliability Scoring**: Identifies unstable or high-latency tools.
- **Zero External Dependencies**: Standard library Python 3.9+.

## Quickstart
```python
from client import ToolTelemetryProfilerClient

profiler = ToolTelemetryProfilerClient()
profiler.record_call("api_fetch", 85.0, True)
info = profiler.get_tool_profile("api_fetch")
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
