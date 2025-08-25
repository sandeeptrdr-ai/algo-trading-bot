import os
import requests
import time
import hmac
import hashlib

# Delta API credentials from GitHub Secrets
API_KEY = os.getenv("oaapvxp9hASiiRcb3BHONF28BCjecp")
API_SECRET = os.getenv("dnd3A9qlw9VuDqh1NNYbdPIHf2s3dN6UjuzvWCCevdGZ11ElPFuJaj6hAHct")

BASE_URL = "https://api.delta.exchange"

# Function to generate signature for private requests
def generate_signature(payload, secret):
    return hmac.new(
        secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

# Example: Get account balances
def get_account_balance():
    url = BASE_URL + "/v2/wallet/balances"
    timestamp = str(int(time.time() * 1000))
    payload = f"{timestamp}GET/api/v2/wallet/balances"
    signature = generate_signature(payload, API_SECRET)

    headers = {
        "api-key": API_KEY,
        "timestamp": timestamp,
        "signature": signature
    }

    response = requests.get(url, headers=headers)
    return response.json()

# Run test
if __name__ == "__main__":
    print("🔗 Testing Delta Exchange Connection...")
    print(get_account_balance())
