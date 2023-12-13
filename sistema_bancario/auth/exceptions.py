from dataclasses import dataclass


@dataclass
class PasswordWek(Exception):
    mensaje: str
