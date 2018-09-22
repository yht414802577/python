import os,sys,time
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0,BASE_PATH)
import unittest, HTMLTestRunner,xmlrunner
from conf.setting import CASE_PATH,HTML_path,XML_path
from BeautifulReport import BeautifulReport
def html_run():
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover(CASE_PATH,'*.py')
    for case in all_cases:
        suite.addTests(case)
    file_name = os.path.join(HTML_path,'%s_report.html'%time.strftime('%Y%m%d%H%M%S'))
    fw = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw)
    runner.run(suite)

def xml_run():
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover(CASE_PATH,'*.py')
    for case in all_cases:
        suite.addTests(case)
    runner = xmlrunner.XMLTestRunner(output=XML_path)
    runner.run(suite)

def run():
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover(CASE_PATH, '*.py')
    for case in all_cases:
        suite.addTests(case)
    result = BeautifulReport(suite)
    result.report(filename='%s_report.html'%time.strftime('%Y%m%d%H%M%S'), description='测试deafult报告', log_path=HTML_path)
# html_run()
# xml_run()
run()