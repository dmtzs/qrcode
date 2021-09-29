<p align="center">
  <img width="280" src="https://github.com/dmtzs/qrcode/blob/master/assets/qrIma.png" alt="logo">
  <h1 align="center" style="margin: 0 auto 0 auto;">QR Code</h1>
  <h5 align="center" style="margin: 0 auto 0 auto;">QR code generator</h5>
</p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/dmtzs/qrcode">
    <img src="https://img.shields.io/github/contributors/dmtzs/qrcode">
    <img src="https://img.shields.io/github/issues/dmtzs/qrcode?label=issues">
    <img src="https://img.shields.io/github/stars/dmtzs/qrcode">
</p>

## The project
This is a project with a tkinter GUI in which you can get qr code images for add them in the projects you want.
<br>
You can download the code or just the executable file of this app in order to run it in your personal computer for your projects.

## Documentation
This is still on development at the wiki part

## Installation, libraries and considerations
For the creation of the exe file execute the next command in windows only:
```
pyinstaller --noconfirm --onefile --windowed --icon "D:/github projects/qrcode/assets/qrIma.ico" --add-data "D:/github projects/qrcode/assets/qrIma.ico;."  "D:/github projects/qrcode/tkqrcode.py"
```