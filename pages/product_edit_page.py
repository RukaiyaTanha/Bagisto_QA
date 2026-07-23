from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.logger import setup_logger
import config


logger = setup_logger()


class ProductEditPage:

    PRODUCT_NAME_FIELD = (By.ID, "name")
    URL_KEY_FIELD = (By.ID, "url_key")
    PRICE_FIELD = (By.ID, "price")
    WEIGHT_FIELD = (By.ID, "weight")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Save Product')]")

    SHORT_DESCRIPTION_IFRAME = (By.ID, "short_description_ifr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self, product_id):
        url = f"{config.ADMIN_URL}/catalog/products/edit/{product_id}"
        logger.info(f"Opening product edit page: {url}")
        self.driver.get(url)

    def enter_product_name(self, name):
        logger.info(f"Updating product name: {name}")
        field = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_FIELD))
        field.clear()
        field.send_keys(name)

    def enter_url_key(self, url_key):
        logger.info(f"Entering URL key: {url_key}")
        field = self.wait.until(EC.visibility_of_element_located(self.URL_KEY_FIELD))
        field.clear()
        field.send_keys(url_key)

    def enter_price(self, price):
        logger.info(f"Entering price: {price}")
        field = self.wait.until(EC.visibility_of_element_located(self.PRICE_FIELD))
        field.clear()
        field.send_keys(price)

    def enter_weight(self, weight):
        logger.info(f"Entering weight: {weight}")
        field = self.wait.until(EC.visibility_of_element_located(self.WEIGHT_FIELD))
        field.clear()
        field.send_keys(weight)

    def enter_short_description(self, text):
        logger.info(f"Entering short description: {text}")

        self.driver.switch_to.default_content()

        self.driver.execute_script("""
        let editor = tinymce.get('short_description');

        if (editor) {
            editor.setContent(arguments[0]);
            editor.fire('change');
            editor.save();
        }
    """, text)

        time.sleep(1)

    def get_short_description_text(self):
        iframe = self.wait.until(EC.presence_of_element_located(self.SHORT_DESCRIPTION_IFRAME))
        self.driver.switch_to.frame(iframe)

        body = self.driver.find_element(By.TAG_NAME, "body")
        text = body.text

        self.driver.switch_to.default_content()
        return text

    def save_product(self):
        logger.info("Saving product changes")
        button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()

    DESCRIPTION_IFRAME = (By.ID, "description_ifr")


    def enter_description(self, text):
        logger.info(f"Entering description: {text}")

        self.driver.switch_to.default_content()

        self.driver.execute_script("""
        let editor = tinymce.get('description');

        if (editor) {
            editor.setContent(arguments[0]);
            editor.fire('change');
            editor.save();
        }
    """, text)

        time.sleep(1)


    def get_description_text(self):
        iframe = self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_IFRAME))
        self.driver.switch_to.frame(iframe)

        body = self.driver.find_element(By.TAG_NAME, "body")
        text = body.text

        self.driver.switch_to.default_content()
        return text
    

    
    