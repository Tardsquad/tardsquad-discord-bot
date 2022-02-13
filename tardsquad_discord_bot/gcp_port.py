import logging
import socket
import threading


def start_server(port):
    logger = logging.getLogger("gcp_port")
    logger.info(f"Will bind socket and listen on TCP localhost:{port}")

    sock = socket.socket()
    sock.bind(("", port))
    sock.listen(8)
    while True:
        conn, addr = sock.accept()
        logger.info(f"Got connection from {addr}")
        conn.send(
            (
                "Thank you for connecting, but we're only listening here because Google Cloud Run "
                "requires us to do. Nothing to do...\n"
            ).encode()
        )
        conn.close()


def start_gcp_port(port):
    """Listen on a given TCP port in a separate thread.

    This is really a dummy TCP listener needed because Google Cloud Run requires the service
    to listen to the from envionment specified $PORT.
    Reference: https://emilwypych.com/2020/10/25/how-to-run-discord-bot-on-cloud-run/
    """
    logger = logging.getLogger("gcp_port")
    logger.info("Spawning of a new thread for GCP port listener.")

    daemon = threading.Thread(name="daemon_server", target=start_server, args=(port,), daemon=True)
    daemon.start()
