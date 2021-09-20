import qrcode

img = qrcode.make("http://192.168.2.204:8800/11.png")
img.save("prodimage2.jpg")