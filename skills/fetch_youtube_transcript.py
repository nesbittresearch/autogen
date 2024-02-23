from autogen.skills import BaseSkill
import requests
import json
from typing import Optional


class YouTubeSkill(BaseSkill):
    def fetch_youtube_transcript(self, video_id: str, api_key: str) -> Optional[str]:
        """
        Fetches the transcript of a YouTube video.

        Args:
            video_id (str): The ID of the YouTube video.
            api_key (str): The YouTube Data API v3 key.

        Returns:
            Optional[str]: The transcript of the video, or None if any error occurs or transcript is not available.
        """
        try:
            url = f"https://www.googleapis.com/youtube/v3/captions/{video_id}?key={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                if "items" in data and len(data["items"]) > 0:
                    return data["items"][0]["snippet"]["text"]
                else:
                    return None
            else:
                return None
        except Exception:
            return None
