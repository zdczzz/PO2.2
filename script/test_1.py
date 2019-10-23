import pytest,allure
class Test_a():
    @allure.step(title='NO.1')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        allure.attach('aaaaa','123')
        assert 1



if __name__ == '__main__':
    pytest.main()

