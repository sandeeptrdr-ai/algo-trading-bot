import os
import requests

API_KEY = os.getenv("oaapvxp9hASiiRcb3BHONF28BCjecp")
API_SECRET = os.getenv("dnd3A9qlw9VuDqh1NNYbdPIHf2s3dN6UjuzvWCCevdGZ11ElPFuJaj6hAHct")

print("🔗 Testing Delta Exchange Connection...")

url = "https://api.delta.exchange/v2/wallet/balances"
headers = {
    "api-key": API_KEY,
    "api-secret": API_SECRET
}

try:
    resp = requests.get(url, headers=headers)
    print("✅ Response:", resp.text)
except Exception as e:
    print("❌ Error:", e)
