from init.Base import Base
import Page as p
class search(Base):
    def search_click(self):
        self.click_element(p.se_btn)

    def search_input(self,text):
        self.input_text(p.text_btn,text)

    def search_bcak(self):
        self.click_element(p.back_btn)