'''
Create a class structure where:
Device (Base class) has method device_info() → prints "This is a device"
Phone (inherits Device) has method call() → prints "Calling..."
Camera (inherits Device) has method click_photo() → prints "Photo clicked"
Smartphone (inherits both Phone and Camera) has method browse() → prints "Browsing internet"
Now, create an object of Smartphone and call all methods.
'''
class Device:
    def device_info(self):
        print("This is a device")
class Phone(Device):
    def call(self):
        print("Calling...")       
class Camera(Device):
    def click_photo(self):
        print("Photo clicked")    
class SmartPhone(Phone, Camera):
    def browse(self):
        print("Browsing Internet")
S = SmartPhone()
S.device_info()
S.call()        
S. click_photo()
S.browse()            