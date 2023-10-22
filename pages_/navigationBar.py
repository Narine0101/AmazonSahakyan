from selenium.webdriver.common.by import By


class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        cardbuttonElement = self.driver.find_element(By.ID, "nav-cart-count-container")
        cardbuttonElement.click()


