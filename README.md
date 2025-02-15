# PyHack

## Overview

PyHack is a Python project focused on automating customer engagement through outbound calls. It uses AI to deliver personalized interactions, reducing the need for human intervention. The project is designed for the BFSI sector, ensuring smooth integration with CRM systems.

## Key Components

- **text_to_speech.py**: Converts text prompts into speech using an external API.
- **EH_agent.py**: Simulates a Sales Development Representative handling customer calls.
- **server.py**: Sets up a server with tools and resources for operations.
- **speech_to_text.py**: Handles audio input and processes it for further use.

## Installation

Ensure Python 3.12+ is installed. Use the `uv` package manager to sync dependencies:

```bash
uv sync
```

## Usage    

To run the project, use the following command:

```bash
uv run EH_agent.py
```

## Project Structure

The project is organized into the following files:

- `EH_agent.py`: Main script for the Sales Development Representative agent.
- `text_to_speech.py`: Converts text prompts into speech.
- `speech_to_text.py`: Handles audio input and processes it for further use.        
