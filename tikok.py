import time

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.ss.android.ugc.aweme', # 启动APP Package名称
  'appActivity': '.main.MainActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element(By.ACCESSIBILITY_ID, '搜索').click()
time.sleep(1)
sbox = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
time.sleep(1)
sbox.send_keys('Unee彤彤')
time.sleep(1)
driver.find_element(By.ACCESSIBILITY_ID, '搜索').click()
time.sleep(2)

driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]').click()
time.sleep(2)
driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/title').click()
time.sleep(2)
driver.find_element(By.ACCESSIBILITY_ID, '用户头像').click()
time.sleep(2)
for i in range(100000):
    driver.tap([(320, 480)], 10)
    time.sleep(0.1)
    driver.tap([(350, 500)], 10)
    time.sleep(0.1)

input('**** Press to quit..')
driver.quit()