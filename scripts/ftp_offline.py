
import io
import os
import sys
from ftplib import FTP

ACTION = sys.argv[1]
HOST = os.environ["FTP_SERVER"]
USER = os.environ["FTP_USERNAME"]
PASSWORD = os.environ["FTP_PASSWORD"]
DIRECTORY = os.environ["FTP_SERVER_DIR"]

OFFLINE_FILE = "app_offline.htm"

with FTP(HOST, timeout=30) as ftp:
    ftp.login(USER, PASSWORD)
    ftp.cwd(DIRECTORY)

    if ACTION == "enable":
        content = (
            b"<html><body>"
            b"<h2>Website is being updated.</h2>"
            b"<p>Please try again shortly.</p>"
            b"</body></html>"
        )

        ftp.storbinary(
            f"STOR {OFFLINE_FILE}",
            io.BytesIO(content)
        )
        print("Application offline file uploaded.")

    elif ACTION == "disable":
        ftp.delete(OFFLINE_FILE)
        print("Application offline file removed.")

    else:
        raise ValueError("Invalid action")
