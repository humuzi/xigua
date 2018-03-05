# coding=utf-8
import unittest
import os
import HtmlTestRunner

# 用例路径
case_path = os.path.join(os.getcwd(),"test_case")
# 报告存放路径
report_path = os.path.join(os.getcwd(),"reports")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    report_abspath = os.path.join(report_path,"report.html")
    with open(report_abspath,"w") as f:
        runner = HtmlTestRunner.HTMLTestRunner(output='test_report',
                                               stream=f,
                                                report_title=u"自动化测试报告",
                                                descriptions=u"用例执行结果:")
        runner.run(all_case())
