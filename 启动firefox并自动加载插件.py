from selenium import webdriver   # 导入webdriver包  
  
driver = webdriver.Firefox()    # 初始化一个火狐浏览器实例：driver  
  
driver.maximize_window()        # 最大化浏览器  
  
driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点  
  
driver.quit()

'''启动firefox并自动加载插件'''

from selenium import webdriver

# 首先找到firefox插件的路径，打开命令行 Windows+R 输入  %APPDATA%\Mozilla\Firefox\Profiles\  (直接打开插件的路径）
# 配置firefox插件路径  ghabrxnf.default  注意：名称不一样，但都是已default为后缀名
profile_directory=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\jydb3xyo.default-1519043279741'
# 加载插件配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)

#--------------------------------------
