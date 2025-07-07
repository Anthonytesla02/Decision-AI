#!/usr/bin/env python3
"""
Script to inject environment variables into config.js
"""
import os

# Get environment variables
paystack_public_key = os.getenv('PAYSTACK_PUBLIC_KEY', '')
paystack_secret_key = os.getenv('PAYSTACK_SECRET_KEY', '')

# Create config.js content
config_content = f"""window.APP_CONFIG = {{ 
    MISTRAL_API_KEY: 'j4h3leTe769ILXBLzwsMkrKEzWqZjOTj',
    PAYSTACK_PUBLIC_KEY: '{paystack_public_key}',
    PAYSTACK_SECRET_KEY: '{paystack_secret_key}'
}};"""

# Write to config.js
with open('config.js', 'w') as f:
    f.write(config_content)

print(f"Config updated with Paystack keys")
print(f"Public key: {paystack_public_key[:20]}..." if paystack_public_key else "No public key found")