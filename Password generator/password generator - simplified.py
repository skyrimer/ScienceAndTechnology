import secrets
import pyperclip
from pywebio import start_server
from pywebio.output import put_button, put_table, put_text, put_warning, toast, use_scope


def copy(password):
    """copies the passoword and displaces the notification about it

    Args:
        password (str): passowrd to copy
    """
    pyperclip.copy(password)
    toast("Copied to clipboard!", duration=1, color='success')

# the decorator below will update the box with password
# hence, only the last passowrd will be visible


@use_scope('scope1', clear=True)
def generate():
    """generate password and desplay the box with outcome
    """
    # here you generate the password anyhow you want
    password = secrets.token_hex(10)
    # this will desplay the box with the password
    # put_text() will show the passoword
    # put_text() will show the button, which will copy password

    put_warning(put_text(password),
                put_button("Copy password",
                           onclick=lambda: copy(password),
                           color='light'))


def main():
    put_text("🔑 Password generator 🔑")
    put_button("Generate random password", onclick=generate)


if __name__ == '__main__':
    start_server(main, 5000, debug=True)
