from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# FTP Server Configuration
FTP_USER = "admin"
FTP_PASS = "123456"
FTP_DIR = "C:\\Users\suchith\Downloads"  # Change this to your desired directory
FTP_PORT = 9999

# Create user and set permissions
authorizer = DummyAuthorizer()
# authorizer.add_user(FTP_USER, FTP_PASS, FTP_DIR, perm="elradfmw")
authorizer.add_anonymous(FTP_DIR, perm="elradfmw")  # Optional: Allow anonymous access

# Setup FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Start FTP server
server = FTPServer(("192.168.1.10", FTP_PORT), handler)
print(f"Starting FTP server on port {FTP_PORT}...")
server.serve_forever()


"""
Steps to Run:
Install pyftpdlib if you haven't already:
bash
Copy code
pip install pyftpdlib
Run the script.
The FTP server will start on port 21, allowing connections with ftpuser and password.
Modify FTP_DIR, FTP_USER, and FTP_PASS as needed. Let me know if you need enhancements! """
