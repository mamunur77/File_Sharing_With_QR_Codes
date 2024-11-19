# Import essential libraries
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# Import png module to enable saving QR codes as PNG
import png

# Specify the port number for the local server
SERVER_PORT = 8080

# Set the working directory
os.chdir(r"M:\WALLPAPER")

# Define the HTTP request handler
RequestHandler = http.server.SimpleHTTPRequestHandler

# Obtain the system's hostname
system_name = socket.gethostname()

# Discover the local IP address of the machine
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # Ping Google's DNS to get the local IP
    sock.connect(("8.8.8.8", 80))
    local_ip = sock.getsockname()[0]
finally:
    sock.close()

# Construct the server URL
server_url = f"http://{local_ip}:{SERVER_PORT}"

# Generate a QR code for easy access to the server URL
qr_code = pyqrcode.create(server_url)
qr_code.svg("server_link.svg", scale=8)  # Save as SVG
qr_code.png("server_link.png", scale=8)  # Save as PNG

# Automatically open the generated QR code in the default web browser
webbrowser.open('server_link.svg')

# Set up the HTTP server to serve files on the specified port
with socketserver.TCPServer(("", SERVER_PORT), RequestHandler) as server:
    print(f"Server is running on port {SERVER_PORT}")
    print(f"Access it via browser: {server_url}")
    print("Alternatively, scan the QR code (server_link.svg or server_link.png)")
    server.serve_forever()
