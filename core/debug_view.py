from django.http import HttpResponse
from django.conf import settings
import requests
import uuid
import json

def debug_payment(request):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied: Superuser required", status=403)
        
    debug_info = []
    debug_info.append(f"<h1>Cashfree Debug Info</h1>")
    
    # 1. Check Settings
    debug_info.append(f"<h3>1. Configuration</h3>")
    debug_info.append(f"<b>CASHFREE_MODE:</b> {getattr(settings, 'CASHFREE_MODE', 'Not Set')}<br>")
    debug_info.append(f"<b>CASHFREE_API_URL:</b> {getattr(settings, 'CASHFREE_API_URL', 'Not Set')}<br>")
    
    key = getattr(settings, 'CASHFREE_API_KEY', '')
    secret = getattr(settings, 'CASHFREE_SECRET_KEY', '')
    
    debug_info.append(f"<b>API Key:</b> {key[:5]}...{key[-3:] if len(key)>5 else ''} (Length: {len(key)})<br>")
    debug_info.append(f"<b>Secret Key:</b> {secret[:5]}...{secret[-3:] if len(secret)>5 else ''} (Length: {len(secret)})<br>")

    # 2. Test Connection
    debug_info.append(f"<h3>2. API Connection Test</h3>")
    
    headers = {
        "Content-Type": "application/json",
        "x-api-version": getattr(settings, 'CASHFREE_API_VERSION', '2023-08-01'),
        "x-client-id": key,
        "x-client-secret": secret
    }
    
    payload = {
        "order_id": f"DEBUG_{str(uuid.uuid4())[:8]}",
        "order_amount": 10.0,
        "order_currency": "INR",
        "customer_details": {
            "customer_id": "DEBUG_USER",
            "customer_name": "Debug Tester",
            "customer_email": "debug@example.com",
            "customer_phone": "9999999999"
        },
        "order_meta": {
            "return_url": "https://example.com/callback",
            "notify_url": "https://example.com/callback"
        }
    }
    
    try:
        url = f"{getattr(settings, 'CASHFREE_API_URL', '')}/orders"
        debug_info.append(f"Sending Request to: <b>{url}</b><br>")
        
        response = requests.post(url, json=payload, headers=headers)
        
        color = "green" if response.status_code == 200 else "red"
        debug_info.append(f"Status Code: <b style='color:{color}'>{response.status_code}</b><br>")
        debug_info.append(f"Response Body: <pre>{json.dumps(response.json(), indent=2)}</pre><br>")
        
    except Exception as e:
        debug_info.append(f"EXCEPTION: <b style='color:red'>{str(e)}</b><br>")

    return HttpResponse("".join(debug_info))
