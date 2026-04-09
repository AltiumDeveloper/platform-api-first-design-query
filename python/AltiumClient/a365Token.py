"""Resources for generating A365 tokens."""
import os

import requests

PROD_TOKEN_URL = "https://auth.altium.com/connect/token"

def get_access_token_using_refresh_token(client_id, client_secret, refresh_token, scopes):
    """Return the A365 token from a refresh token."""

    token = {}
    try:
        token = requests.post(
            url = os.environ.get('TOKEN_URL') or PROD_TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": " ".join(scopes)
            },
        ).json()

    except Exception:
        raise

    return token
