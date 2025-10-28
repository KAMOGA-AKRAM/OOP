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






