import socket
from constants import HOST, PORT

# Client main function
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = s.recv(4096).decode()
            if not data:
                break

            # Handle input prompts
            if data.strip().endswith("Your answer (1-4):") or data.strip().endswith("Enter your name:"):
                ans = input(data)
                s.sendall(ans.strip().encode())
            else:
                print(data)


if __name__ == "__main__":
    main()
