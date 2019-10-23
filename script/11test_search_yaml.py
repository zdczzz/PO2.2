from init.init_driver import init_driver
from Page.page_search_yaml import search
from init.read_data import read_yaml
import pytest
# def test_data():
#     data = ret_yaml("search_data").get('Search_Data')
#     data_list=[]
#     for i in data.values():
#         data_list.append(i.get('test'))
#     return data_list
def test_data():
    data = read_yaml('search_data').get('Search_Data')
    data_list = []
    for i in data.values():
        data_list.append(i.get('test'))
    return data_list



class Test_yaml():
    def setup_class(self):
        self.driver = init_driver()
        self.ss = search(self.driver)
    def teardown_class(self):
        self.driver.quit()

    def test_1(self):
        self.ss.search_click()
    @pytest.mark.parametrize('text',test_data())
    def test_2(self,text):
        self.ss.search_input(text)

    def test_3(self):
        self.ss.search_bcak()

if __name__ == '__main__':
    pytest.main()