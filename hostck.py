import ssl
import socket
import time

# Input & Output files
HOST_FILE = "host.txt"
WORKING_SNI_FILE = "working_sni_zoom.txt"

# Original VLESS link
VLESS_TEMPLATE = "vless://42d69a27-4249-442d-f63f-7bbc78c8bfb9@skynetconfigs.duckdns.org:443?type=tcp&security=tls&fp=chrome&alpn=&allowInsecure=1&sni={}"

def check_sni(host, port=443, timeout=5):
    """
    Checks if an SNI is valid by establishing an SSL connection.
    Returns True if the server responds correctly.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                return True
    except (ssl.SSLError, socket.error):
        return False
    return False

def test_latency(host):
    """
    Measures latency using a TCP connection.
    """
    try:
        start = time.time()
        socket.create_connection((host, 443), timeout=5).close()
        return round((time.time() - start) * 1000, 2)  # Convert to ms
    except socket.error:
        return None

def main():
    try:
        with open(HOST_FILE, "r") as f:
            hosts = [line.strip() for line in f if line.strip()]

        working_snies = []

        for sni in hosts:
            print(f"Testing SNI: {sni}...")
            if check_sni(sni):
                latency = test_latency(sni)
                print(f"[✔] {sni} works! Latency: {latency}ms")
                working_snies.append(f"{sni}")
            else:
                print(f"[✘] {sni} failed.")

        # Save working SNIs
        with open(WORKING_SNI_FILE, "w") as f:
            f.write("\n".join(working_snies))

        print(f"\n✅ Working SNIs saved to {WORKING_SNI_FILE}")

    except FileNotFoundError:
        print(f"❌ Error: {HOST_FILE} not found.")

if __name__ == "__main__":
    main()
