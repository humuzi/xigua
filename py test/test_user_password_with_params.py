# coding = utf-8
import pytest
import json

data_file_path = "./user_data.json"
with open(data_file_path) as f:
    users = json.loads(f.read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self,request):
        return request.param

    def test_user_password(self,user):
        passwd = user["password"]
        assert len(passwd) >= 6
        msg = "user %s has a week password %s"%(user["name"],user["password"])
        assert passwd != "password",msg
        assert passwd != "password123",msg

if __name__ == '__main__':
    pytest.main("-q test_user_password_with_params.py")

