from init.init_driver import init_driver
from Page.Page_Main import Page_Main
import pytest
import Page as p

class Test_Search():

    def setup_class(self):
        self.driver = init_driver()
        self.ps = Page_Main(self.driver).Search()

    def teardown_class(self):
        self.driver.quit()

    def test_click(self):
        self.ps.click_search()
        text = self.ps.find_element(p.text_info).text
        assert text=='搜索…','没找到！！！！！！！！！！'

    @pytest.mark.parametrize('text',['1','2'])
    def test_input(self,text):
        self.ps.input_search(text)
        text1 = self.ps.find_element(p.text_info).text
        assert text1 == text,'no find!!!!!'


    def test_back(self):
        self.ps.back_search()
        text = self.ps.find_element(p.text_tit).text
        assert text =='设置','没有返回成功'

if __name__ == '__main__':
    pytest.main()