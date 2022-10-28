import __init
import tool
import pytest


class Test_ABC():

    # 函数级开始
    def setup(self):
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        print("------->teardown_method")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    # assert a == "yoyo"  # fixture失败就是error
    return a


def test_1(user):
    assert user == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_run.py"])

    import pytest


    @pytest.fixture(scope='function', autouse=True)  # 作用域设置为function，自动运行
    def before():

        print("------->before")


    class Test_ABC:

        def setup(self):
            print("------->setup")

        def test_a(self):
            print("------->test_a")

            assert 1

        def test_b(self):
            print("------->test_b")

            assert 1


    if __name__ == '__main__':
        pytest.main("-s  test_abc.py")

执行结果：

test_abc.py

------->before  # 运行第一次

------->setup

------->test_a

.------->before  # 运行第二次

------->setup

------->test_b

.
