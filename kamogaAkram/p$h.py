class Gadget:
    def start(self):
        print("Gadget started.")

class phone(Gadget):
    def start(self):
        print("Phone is starting with a Hello.")


class Laptop(Gadget):
    def start(self):
        print("Laptop is booting up.")

gadgets = [phone(), Laptop()]
for gadget in gadgets:
    gadget.start()

class Camera:
    def take_photo(self):
        print("Photo taken.")

class WifiEnabled:
    def connect_wifi(self):
        print('connected to Wifi')

class SmartPhone(phone,Camera,WifiEnabled):
    def start(self):
        print("WELCOME.")

class SmartPrinter(Gadget,WifiEnabled):
    def start(self):
        print("Smart Printer is ready to print.")

devices = [SmartPhone(), SmartPrinter()]
for device in devices:
    device.start()
    if isinstance(device, WifiEnabled):
        device.connect_wifi()   
    if isinstance(device, Camera):
        device.take_photo()




