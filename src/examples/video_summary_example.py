# filepath: lmstudio-client/src/examples/video_summary_example.py
from lmstudio_client.client import LMStudioClient

def main():
    api_key = "your_api_key_here"  # Replace with your actual API key
    video_info = {
        'filename': 'example_video.mp4',
        'total_duration': 120.0,
        'scenes_detected': 5,
        'scenes': [
            {'scene_index': 0, 'start_time': 0.0, 'end_time': 30.0, 'text_content': 'Introduction to the topic.'},
            {'scene_index': 1, 'start_time': 30.0, 'end_time': 60.0, 'text_content': 'Detailed explanation of the first concept.'},
            {'scene_index': 2, 'start_time': 60.0, 'end_time': 90.0, 'text_content': 'Discussion of related ideas.'},
            {'scene_index': 3, 'start_time': 90.0, 'end_time': 110.0, 'text_content': 'Conclusion and summary of key points.'},
            {'scene_index': 4, 'start_time': 110.0, 'end_time': 120.0, 'text_content': 'Final thoughts and call to action.'}
        ]
    }

    client = LMStudioClient(api_key)
    
    summary = client.generate_summary(video_info)
    print("Generated Summary:")
    print(summary)

    notes = client.generate_notes(video_info)
    print("\nGenerated Notes:")
    print(notes)

if __name__ == "__main__":
    main()