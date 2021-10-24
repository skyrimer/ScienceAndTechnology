import secrets
import pyperclip
from pywebio import start_server
from pywebio.output import clear, put_button, put_table, put_text, put_warning, toast, use_scope


def copy(password):
    pyperclip.copy(password)
    toast("Copied to clipboard!", duration=2, color='success')


@use_scope('scope1', clear=True)
def generate():
    password = secrets.token_hex(10)
    put_warning(put_text(password),
                put_button("Copy password",
                           onclick=lambda: copy(password),
                           color='light'))


def main():
    put_text("🔑 Passoword generator 🔑")
    put_button("Generate random passoword", onclick=generate)


if __name__ == '__main__':
    start_server(main, 5000, debug=True)
