#!/usr/bin/env python3
import os
import json
import http.server
import socketserver
import urllib.parse

class ConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/config':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            config = {
                'PAYSTACK_PUBLIC_KEY': os.getenv('PAYSTACK_PUBLIC_KEY', ''),
                'PAYSTACK_SECRET_KEY': os.getenv('PAYSTACK_SECRET_KEY', '')
            }
            
            self.wfile.write(json.dumps(config).encode())
            return
        
        # Default file serving
        super().do_GET()

if __name__ == "__main__":
    PORT = 5001
    with socketserver.TCPServer(("127.0.0.1", PORT), ConfigHandler) as httpd:
        print(f"Config server running on port {PORT}")
        httpd.serve_forever()