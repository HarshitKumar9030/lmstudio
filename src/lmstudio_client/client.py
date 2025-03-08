import json
import requests
import time
import sys
import os

# Fix imports for both package and direct execution
try:
    # When running as part of the package
    from .exceptions import LMStudioAPIError, LMStudioInvalidResponseError, LMStudioRequestError
    from .utils import format_prompt, format_notes
except ImportError:
    # When running directly
    from lmstudio_client.exceptions import LMStudioAPIError, LMStudioInvalidResponseError, LMStudioRequestError
    from lmstudio_client.utils import format_prompt, format_notes

class LMStudioClient:
    """Client for interacting with LM Studio's API with an OpenAI-compatible interface."""
    
    def __init__(self, api_key=None, base_url="http://localhost:1234/v1"):
        """Initialize the LM Studio client.
        
        Args:
            api_key: Optional API key (not required for local LM Studio servers)
            base_url: Base URL for the LM Studio server, defaults to localhost:1234
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"
    
    def generate_summary(self, video_info):
        """Generate a summary of the video using LM Studio model.
        
        Args:
            video_info: Dictionary containing video information
            
        Returns:
            String containing the generated summary
            
        Raises:
            LMStudioAPIError: If video_info is None or invalid
        """
        if video_info is None:
            raise LMStudioAPIError("Summary generation failed: video_info cannot be None")
            
        try:
            prompt = format_prompt(video_info)
            
            response = self._generate_completion(prompt)
            
            # Add a small delay to allow cleanup
            time.sleep(0.1)
            return response
                
        except Exception as e:
            print(f"Error in LM Studio API: {str(e)}")
            raise LMStudioAPIError(f"Summary generation failed: {str(e)}")
    
    def generate_notes(self, processed_data):
        """Generate detailed notes from the video data.
        
        Args:
            processed_data: Dictionary containing processed video data
            
        Returns:
            String containing the generated notes
            
        Raises:
            LMStudioAPIError: If processed_data is None or invalid
        """
        if processed_data is None:
            raise LMStudioAPIError("Notes generation failed: processed_data cannot be None")
            
        try:
            prompt = format_notes(processed_data)
            
            response = self._generate_completion(prompt)
            
            # Add a small delay to allow cleanup
            time.sleep(0.1)
            return response
                
        except Exception as e:
            print(f"Error in LM Studio API: {str(e)}")
            raise LMStudioAPIError(f"Notes generation failed: {str(e)}")
    
    def _generate_completion(self, prompt, model=None, max_tokens=2048, temperature=0.7):
        """Generate completion using the LM Studio API.
        
        Args:
            prompt: The prompt to send to the model
            model: Optional model name (uses default if not specified)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text response
        """
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        if model:
            payload["model"] = model
            
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                else:
                    raise LMStudioInvalidResponseError("Invalid response format")
            else:
                raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
    
    def list_models(self):
        """List available models from LM Studio server.
        
        Returns:
            List of available models
        """
        endpoint = f"{self.base_url}/models"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            
            if response.status_code == 200:
                return response.json()
            else:
                raise LMStudioRequestError(f"Failed to list models: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")