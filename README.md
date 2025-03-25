# Medullar MCP Server

A server for retrieving Medullar Space data using the MCP protocol.

## Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended)
- A Medullar JWT token

## Setup

1. Install dependencies using `uv`:
```bash
brew install uv
uv pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your Medullar JWT:
```bash
MEDULLAR_JWT=your_jwt_token_here
```

## Running Your Server

### Development Mode

The fastest way to test and debug your server is with the MCP Inspector:

```bash
mcp dev server.py
```

### Production Installation

Once your server is ready, install it in Claude Desktop:

```bash
mcp install server.py
```

### Direct Execution

For advanced scenarios like custom deployments:

```bash
python server.py
# or
mcp run server.py
```

## Environment Variables

The server requires the following environment variables:
- `MEDULLAR_JWT`: Your Medullar authentication token

These can be provided either through:
- A `.env` file in the project root
- Environment variables in your shell
- The `mcp install` command with the `-v` flag

## API Endpoints

The server provides the following endpoints:

### get_medullar_spaces
Retrieves the user's Medullar spaces, which contain their curated data.

Returns a list of spaces in the format:
```json
[
    {
        "name": "Space Name",
        "uuid": "Space unique identification",
        "context": "Space context"
    }
]
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.