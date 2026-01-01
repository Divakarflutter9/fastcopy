import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("CASHFREE_API_KEY")
SECRET_KEY = os.getenv("CASHFREE_SECRET_KEY")
API_URL = os.getenv("CASHFREE_API_URL")

print(f"API URL: {API_URL}")
print(f"API Key: {API_KEY[:5]}..." if API_KEY else "No API Key")

headers = {
    "Content-Type": "application/json",
    "x-api-version": "2023-08-01",
    "x-client-id": API_KEY,
    "x-client-secret": SECRET_KEY
}

import uuid

payload = {
    "order_id": f"TEST_{str(uuid.uuid4())[:8]}",
    "order_amount": 100.0,
    "order_currency": "INR",
    "customer_details": {
        "customer_id": "CUST_TEST_001",
        "customer_name": "Test User",
        "customer_email": "test@example.com",
        "customer_phone": "9999999999"
    },
    "order_meta": {
        "return_url": "https://example.com/callback",
        "notify_url": "https://example.com/callback"
    }
}

try:
    with open('api_result.log', 'w') as f:
        f.write("Sending request to Cashfree...\n")
        response = requests.post(f"{API_URL}/orders", json=payload, headers=headers)
        f.write(f"Status Code: {response.status_code}\n")
        f.write("Response Body:\n")
        f.write(json.dumps(response.json(), indent=2))
        f.write("\n")
except Exception as e:
    with open('api_result.log', 'w') as f:
        f.write(f"Error: {e}\n")
