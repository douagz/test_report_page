import pytest,os
from config.config import Config


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir
    os.system(f"del {os.path.join(Screenshot, '*.png')}")
    #pytest.main(["-vs", 'tests', f'--alluredir={AllureResult}', "--clean-alluredir"])
    #os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')
    root_dir = os.path.split(__file__)[0]
    test_report_dir = root_dir + os.path.sep + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + os.path.sep + "AllureResult"
    pytest.main(["-vs", 'AllureTest', f'--alluredir={test_result_dir}', "--clean-alluredir"])
    os.system(f'allure generate {test_result_dir} -o {test_report_dir} --clean')



