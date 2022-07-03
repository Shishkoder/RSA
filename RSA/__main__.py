from console_app import User


def main() -> None:
    a: User = User()
    b: User = User()
    a.send_message("Hello, world#№", b)
    a.send_message("Hi", b)
    a.send_message("Привет!, мир", b)
    for i in range(1, 4):
        print(b.show_message(i))


if __name__ == "__main__":
    main()
