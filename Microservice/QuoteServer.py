
import RandomCall as RandomQuoteFunc
import socket


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 2259 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:  # Server loop to keep listening
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:  # Connection loop to handle each client's requests
                data = conn.recv(1024)
                if not data:
                    print("Client disconnected.")
                    break
                decoded_data = data.decode()
                if decoded_data == 'quote':
                    print(f"Received {data!r}")
                    quote = RandomQuoteFunc.generate_random_quote('')
                    #quote = "Hello"
                    quote_str = str(quote)
                    message = quote_str.encode()
                    conn.sendall(message)
                    print("Data sent:", message)