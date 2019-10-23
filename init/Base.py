from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10,poll=0.5):
        """
        定位元素方法
        :param loc: (By.ID,'xx.andda.ss')
        :param timeout:显示等待超时时间
        :param poll: 检查频率
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def click_element(self,loc):

        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)