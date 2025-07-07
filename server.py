#!/usr/bin/env python3
"""
Simple HTTP server with Paystack configuration endpoint
"""
import os
import json
import http.server
import socketserver
from urllib.parse import urlparse

class PaystackConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        # Handle API endpoint for Paystack configuration
        if parsed_path.path == '/api/paystack-key':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            config = {
                'publicKey': os.getenv('PAYSTACK_PUBLIC_KEY', '')
            }
            
            self.wfile.write(json.dumps(config).encode())
            return
        
        # Handle config.js file with environment variables
        if parsed_path.path == '/config.js':
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            
            config_js = f"""window.APP_CONFIG = {{ 
    MISTRAL_API_KEY: 'j4h3leTe769ILXBLzwsMkrKEzWqZjOTj',
    PAYSTACK_PUBLIC_KEY: '{os.getenv("PAYSTACK_PUBLIC_KEY", "")}',
    PAYSTACK_SECRET_KEY: '{os.getenv("PAYSTACK_SECRET_KEY", "")}'
}};"""
            
            self.wfile.write(config_js.encode())
            return
        
        # Default static file serving
        super().do_GET()

if __name__ == "__main__":
    PORT = int(os.getenv('PORT', 5000))
    
    with socketserver.TCPServer(("0.0.0.0", PORT), PaystackConfigHandler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT}")
        httpd.serve_forever()