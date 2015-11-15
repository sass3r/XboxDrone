import XboxController

def pushButton()
    print "Boton presionado:"

xbox = XboxController.XboxController(
        controllerCallBack = pushButton,
        joystickNo = 0, 
        deadzone = 0.1,
        scale = 1, 
        invertYaxis = False)




