from selenium import webdriver
from selenium_stealth import stealth
import time


class Instance:
	def __init__(self, url):
		self.url = url
		self.options = webdriver.ChromeOptions()
		#self.options.add_argument("start-maximized")
		self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.options.add_experimental_option('useAutomationExtension', False)
		self.driver = webdriver.Chrome(options=self.options)
		stealth(self.driver,
        	languages=["fr-FR", "fr"],
        	vendor="Google Inc.",
        	platform="Win32",
        	webgl_vendor="Intel Inc.",
        	renderer="Intel Iris OpenGL Engine",
        	fix_hairline=True,
        )

	def run(self):
		self.driver.get(self.url)
		time.sleep(10000)
		

x = Instance("https://bot.sannysoft.com")
x.run()