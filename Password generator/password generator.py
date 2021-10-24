import secrets
import pyperclip
from pywebio import start_server
from pywebio.output import clear, put_button, put_table, put_text, put_warning, toast, use_scope

head_style = """
text-align: center;
font-size: 3rem;
color: #d53369;
margin: 2em 0;
"""
button_style = """
text-align: center;
margin-bottom: 1em;
"""
password_style = """
font-size: 1.75em;
color: #000;
font-weight: bold;
font-family: monospace;
letter-spacing: 0.1em;
"""
output_style = """
background: linear-gradient(-45deg, #d53369, #cbad6d);
border: none;
display: flex;
flex-wrap: wrap;
align-items: center;
justify-content: space-around;
gap: 0.5em 1em;
"""


def copy(password):
    pyperclip.copy(password)
    toast("Copied to clipboard!", duration=1, color='success')


@use_scope('scope1', clear=True)
def generate():
    password = secrets.token_hex(10)
    put_warning(put_text(password).style(password_style),
                put_button("Copy password",
                           onclick=lambda: copy(password),
                           color='light'
                           ).style("margin: 0;")
                ).style(output_style)


def main():
    put_text("🔑 Passoword generator 🔑").style(head_style)
    put_button("Generate random passoword",
               onclick=generate).style(button_style)


if __name__ == '__main__':
    start_server(main, 5000, debug=True)
