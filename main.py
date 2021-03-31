import socket


class Checker:
    def __init__(self):
        self.addr = "127.0.0.1"

        with open("input.txt", encoding="utf-8") as data:
            self.start = int(data.readline().strip("\ufeff"))
            self.end = int(data.readline())

        if self.start is None or self.end is None:
            print("Everything is very bad :(")
            print("Your input is wrong.")
            print("It should be two integers in two different lines")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            for i in range(self.start, self.end + 1):
                c = sock.connect_ex(("localhost", i))
                if not c:
                    print(f"this port is available: {i}")


if __name__ == "__main__":
    Checker()
