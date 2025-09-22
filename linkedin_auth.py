import os
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
SCOPES = "w_member_social"

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        if "code" in params:
            code = params["code"][0]
            print(f"Got auth code: {code}")
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET
            }
            r = requests.post(TOKEN_URL, data=data)
            print("Access Token Response:", r.json())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Auth completed. You can close this window.")

if __name__ == "__main__":
    auth_url = f"{AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPES}"
    print(f"Open this URL to authorize:\n{auth_url}")
    webbrowser.open(auth_url)
    server = HTTPServer(("localhost", 8080), OAuthHandler)
    print("Waiting for redirect...")
    server.handle_request()
