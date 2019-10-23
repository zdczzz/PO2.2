from Page.page_search import Search

class Page_Main():
    def __init__(self,driver):
        self.driver =driver

    def Search(self):
        return Search(self.driver)