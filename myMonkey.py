from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

device = MonkeyRunner.waitForConnection()

#device.installPackage('myproject/bin/MyApplication.apk')

package = 'com.android.vending'
#package = 'com.xtek.chatlite'

activity = 'com.android.vending.AssetBrowserActivity'
#activity = 'com.xtek.chatlite.LoginActivity'
runComponent = package + '/' + activity

device.startActivity(runComponent)
MonkeyRunner.sleep(1.0)
device.touch(500, 100, 'DOWN_AND_UP')

wantedAppName = list("busybox")
for letter in wantedAppName:
    device.type(letter)
    MonkeyRunner.sleep(0.5)


MonkeyRunner.sleep(1.0)
device.press('KEYCODE_ENTER', 'DOWN_AND_UP')
#easy_device.touch(By.id('id/input_name'), MonkeyDevice.DOWN_AND_UP)

#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
