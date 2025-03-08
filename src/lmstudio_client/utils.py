import json

def format_prompt(video_info):
    prompt = f"You are a video analysis expert. Create a comprehensive summary and notes for the following video:\n\n"
    prompt += f"Video: {video_info['filename']}\n"
    prompt += f"Duration: {video_info['total_duration']:.2f} seconds\n"
    prompt += f"Scenes detected: {video_info['scenes_detected']}\n\n"

    if 'scenes' in video_info and video_info['scenes']:
        prompt += "## SCENE BREAKDOWN:\n"
        for scene in video_info['scenes']:
            prompt += f"\nScene {scene['scene_index'] + 1} ({scene['start_time']:.2f}s - {scene['end_time']:.2f}s):\n"
            if scene['text_content']:
                prompt += f"Text detected: {scene['text_content'][:500]}...\n" if len(scene['text_content']) > 500 else f"Text detected: {scene['text_content']}\n"

    prompt += """
Based on the above information, please provide:
1. A concise summary of the video content
2. Key points or important information extracted from the video
3. Any notable observations about the structure or content
4. Well-organized notes that could be used for reference

Format your response as a well-structured document with headings, bullet points and proper organization.
"""
    return prompt

def format_notes(processed_data):
    """Format a prompt for generating notes.
    
    Args:
        processed_data: Dictionary containing processed data
        
    Returns:
        Formatted prompt string
        
    Raises:
        TypeError: If processed_data is not a dictionary
    """
    if not isinstance(processed_data, dict):
        raise TypeError("processed_data must be a dictionary")
    
    notes_prompt = f"As an expert note-taker, create detailed, organized notes from this video content. \n"
    notes_prompt += "Focus on creating a hierarchical structure that captures main ideas and supporting details.\n\n"
    
    # Safely convert processed_data to JSON string with a default handler for non-serializable objects
    try:
        data_str = json.dumps(processed_data, indent=2, default=str)[:4000]
    except (TypeError, ValueError):
        data_str = str(processed_data)[:4000]
    
    notes_prompt += f"Content information:\n{data_str}\n\n"
    notes_prompt += "Format your notes as markdown with:\n"
    notes_prompt += "- Clear headings and subheadings\n"
    notes_prompt += "- Bullet points for key concepts\n"
    notes_prompt += "- Numbered lists for sequential information\n"
    notes_prompt += "- Code blocks or tables where appropriate\n"
    notes_prompt += "- Bold text for important terms or concepts\n\n"
    notes_prompt += "Your notes should be comprehensive yet concise, capturing the essence of the content.\n"
    return notes_prompt

def process_response(response):
    """Process an API response and extract the text content"""
    if isinstance(response, dict) and 'text' in response:
        return response['text']
    return 'Response processing failed: No text in response'