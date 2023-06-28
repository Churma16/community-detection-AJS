import tweepy

# api_key = "9iSTstvlgs6g9CZpxB3mVsglY"
# api_secret_key = "lYOeOSrIgqdDkvdYy0T2UUr5GXpn7949RpGBInUazlI8V3oyCF"
# access_token = "1179415333192396800-nvVO3itXroGAkO4r4NnLi6gTaUgTZ0"
# access_token_secret = "KKPbJHePqt3D7husjsbyDk73Bq6e26sVL4QIqLN0ZPSg9"
# # AAAAAAAAAAAAAAAAAAAAANm9nQEAAAAAkUbsn%2BZvXSsRQrydQmBsk9XaznY%3DsCBgM1j0pesATLxnxlfvmJtF4Z17PecXUDUYwELsiLZatRGuuj
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

import requests

# Set the Twitter API endpoint
endpoint = "https://api.twitter.com/2/users/:id/followers"

# Set the Twitter API bearer token
bearer_token = "YOUR_BEARER_TOKEN"

# Set the user ID
user_id = "YOUR_USER_ID"

# Make the request
headers = {"Authorization": "Bearer {}".format(bearer_token)}
response = requests.get(endpoint, headers=headers, params={"user_id": user_id})

# Check the response status code
if response.status_code == 200:
    # Get the follower count
    follower_count = response.json()["data"]["total_count"]
    print("The follower count is:", follower_count)
else:
    print("Error:", response.status_code)