from selenium import webdriver
from selenium.webdriver.common.by import By


class Test333():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_333(self):
        self.driver.get("https://demo.constantadev.tech/fms3/red/dev/")
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1680, 948)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".c-header__icon_menu svg").click()
