from typing import Any
import httpx
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("medullar")

JWT = os.getenv("MEDULLAR_JWT")
if not JWT:
    raise ValueError("MEDULLAR_JWT environment variable is not set")

EXPLORATOR_API_BASE = "https://api.medullar.com/explorator/v1/"


async def make_api_request(url: str, method: str = "GET") -> dict[str, Any] | None:
    """Make a request to the Medullar API with proper error handling."""
    headers = {"Accept": "application/json", "Authorization": f"Bearer {JWT}"}
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, timeout=30.0)
            elif method.upper() == "PUT":
                response = await client.put(url, headers=headers, timeout=30.0)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=headers, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_medullar_spaces() -> list[dict[str, Any]]:
    """
    Get users medullar spaces, where the user stores their source of truth for their data.
    Medullar spaces are a way to organize data for a user.
    They contain data that is relevant to a user and that personally the user has curated.

    Args:
        None

    Returns:
        A dictionary of users medullar spaces with a summary of what they contain in the format:
        [
            {
                    "name": "Space Name",
                    "uuid": "Space unique identification",
                    "context": "Space context",
            }
        ]
    """

    url = f"{EXPLORATOR_API_BASE}/spaces/"
    data = await make_api_request(url)

    if not data:
        return "Unable to fetch spaces."

    if data.get("count") == 0:
        return "No spaces found."

    spaces = []
    for space in data.get("results"):
        spaces.append(
            {
                "name": space.get("name"),
                "uuid": space.get("uuid"),
                "context": space.get("context"),
            }
        )

    return spaces


if __name__ == "__main__":
    # Initialize and run the server
    print("Starting Medullar MCP server...")
    mcp.run(transport="stdio")
