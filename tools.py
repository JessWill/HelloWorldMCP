import anyio
import mcp.types as types

async def register_tools(app):
    @app.call_tool()
    async def call_tool(
        name: str, arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        print("Hey girl, hello!!!")

        return [
            types.TextContent(
                type="text",
                text=(
                    "Hey girl, hello!!!"
                ),
            )
        ]

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="hello-world",
                description=(
                    "Replies hello world from the mcp server"
                ),
                inputSchema={
                    "type": "object",
                    "required": ["message"],
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "A message to say hello back to",
                        },
                    },
                },
            )
        ]
