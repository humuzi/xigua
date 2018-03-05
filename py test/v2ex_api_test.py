# coding = utf-8
import requests
import pytest

class TestV2exApi(object):
    domain = "http://www.v2ex.com/"

    def test_node(self):
        path = "api/nodes/show.json?name=python"
        url = self.domain + path
        res = requests.get(url).json()    #使用requests库来简化发送get请求并将返回值的json字符串转换成python字典
        assert res["id"] == 90
        assert res["name"] == "python"

    # 使用fixture参数化接口入参
    @pytest.fixture(params=['python','java','go','node js'])
    def lang(self,request):
        return request.param   #访问本次传入fixture中的参数
    def test_nodes(self,lang):
        path = "api/nodes/show.json?name = %s"%(lang)
        url = self.domain + path
        res =requests.get(url).json()
        assert res["name"] == lang
        assert 0       #强制用例失败，这样可以看到每次fixture的参数值

    # 使用fixture参数化测试预期结果
    @pytest.mark.parametrize("name,node_id",[('python',90),('java','63'),('go',375),('node js',436)])
    def test_node1(self,name,node_id):
        path ="api/nodes/show.json?name=%s"%(name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res["name"] == name
        assert res["id"] == node_id
        assert 0
if __name__ == '__main__':
    pytest.main("-q v2ex_api_test.py  --junitxml=./log.xml")   # --junitxml=./log.xml 在命令行加入生成测试报告