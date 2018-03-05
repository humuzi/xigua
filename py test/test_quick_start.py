def reverse(string):
    return string[::-1]
def test_reverse():
    string = "good"
    assert reverse(string) == "doog"
    anoher_string = "itest"
    assert reverse(anoher_string) =="tseti"