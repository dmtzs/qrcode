import qrcode
from app import app
from typer import Option


@app.command()
def wifiqr(
    ssid: str = Option(..., help="The SSID of the network."),
    password: str = Option(..., help="The password of the network."),
    encryption: str = Option("WPA", help="The encryption type of the network."),
    hidden: bool = Option(False, help="Whether the network is hidden."),
    ascii: bool = Option(False, help="Print the QR code as ASCII in terminal, otherwise an image will be saved."),
) -> None:
    """
    Generate a QR code for a WiFi network.

    The QR code will contain the SSID, password, encryption, and hidden status.

    Args:
        - ssid (str): The SSID of the network.
        - password (str): The password of the network.
        - encryption (str): The encryption type of the network.
        - hidden (bool): Whether the network is hidden.
    """
    wifi_data = f"WIFI:S:{ssid};T:{encryption};P:{password};H:{int(hidden)};;"
    qr = qrcode.QRCode()
    qr.add_data(wifi_data)
    qr.make()
    if ascii:
        qr.print_ascii(invert=True)
    else:
        qr.make_image(fill_color="black", back_color="white").save("wifi.png")

# comando: python main.py wifiqr --help