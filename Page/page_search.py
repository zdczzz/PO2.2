from init.Base import Base
import Page as p

class Search(Base):

    def click_search(self):
        self.click_element(p.se_btn)

    def input_search(self,text):
        self.input_text(p.text_btn,text)

    def back_search(self):
        self.click_element(p.back_btn)