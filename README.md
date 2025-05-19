# HelloWorldMCP

A small **Hello World** to get me started in the world of **Model Context Protocols (MCP)**. 

This minimal example sets up a simple MCP server using the [python-sdk](https://github.com/modelcontextprotocol/python-sdk) and responds with a greeting whenever a tool is called.
Used https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-streamablehttp-stateless as a template.


### Requirements

- Python 3.10 or later
- [uvicorn](https://www.uvicorn.org/)
- MCP Python SDK

To install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Running the Server
```bash
uv run HelloWorldMCP
```

Then simply connect using something like Claude Desktop or I used 5ire. 
URL should be: http://0.0.0.0:3000/mcp
