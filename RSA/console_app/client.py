from .simple_rsa import RSA


class User:
    def __init__(self) -> None:
        self.__private_key, self.__public_key = RSA.create_keys()
        self.__messages_list: list = []

    def send_message(self, message: str, other_user: object) -> None:
        other_user.__messages_list.append(RSA.encode_message(message, other_user.__public_key))

    def show_message(self, number_message: int) -> str:
        return RSA.decode_message(self.__messages_list[number_message - 1], self.__private_key)
