from selenium.webdriver.common.by import By


class LocatorTypes:
    xpath = By.XPATH
    id = By.ID
    name = By.NAME
    css = "By.CSS_SELECTOR"
    class_name = By.CLASS_NAME
    link_text = By.LINK_TEXT
    partial_link_text = By.PARTIAL_LINK_TEXT
    tag_name = By.TAG_NAME
