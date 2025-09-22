import os
import requests
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def post_to_linkedin(content: str):
    try:
        profile_url = "https://api.linkedin.com/v2/me"
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        r = requests.get(profile_url, headers=headers)
        r.raise_for_status()
        user_urn = r.json()["id"]

        post_url = "https://api.linkedin.com/v2/ugcPosts"
        payload = {
            "author": f"urn:li:person:{user_urn}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": content},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }

        r = requests.post(post_url, json=payload, headers={**headers, "Content-Type": "application/json"})
        r.raise_for_status()
        print(f"Posted to LinkedIn: {content}")
        return {"status": "success"}
    except Exception as e:
        print(f"Error posting to LinkedIn: {e}")
        return {"status": "error", "error": str(e)}
