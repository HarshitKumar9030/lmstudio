# LM Studio Client

## Overview
The LM Studio Client is a Python module designed to simplify interactions with the LM Studio API. It provides an easy-to-use interface for generating summaries and notes from video content, making it ideal for developers and researchers working with video analysis.

## Features
- **Generate Summaries**: Quickly create concise summaries of video content.
- **Detailed Notes**: Generate organized notes with key points and observations.
- **Error Handling**: Custom exceptions for robust error management.
- **Utility Functions**: Helper functions for formatting and processing API responses.

## Installation

### From PyPI (recommended)
```bash
pip install lmstudio-client
```

### From source
```bash
git clone <repository-url>
cd lmstudio-client
pip install -e .
```

## Usage
Here is a simple example of how to use the `LMStudioClient`:

```python
from lmstudio_client import LMStudioClient

# Initialize the client (API key not required for local LM Studio servers)
client = LMStudioClient(base_url="http://localhost:1234/v1")

# Video information
video_info = {
    'filename': 'example_video.mp4',
    'total_duration': 120.0,
    'scenes_detected': 5,
    'scenes': [
        {'scene_index': 0, 'start_time': 0.0, 'end_time': 30.0, 'text_content': 'Introduction'},
        {'scene_index': 1, 'start_time': 30.0, 'end_time': 60.0, 'text_content': 'Main Content'},
        # Add more scenes as needed
    ]
}

# Generate summary
summary = client.generate_summary(video_info)
print(summary)

# List available models
models = client.list_models()
print("Available models:", models)
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.