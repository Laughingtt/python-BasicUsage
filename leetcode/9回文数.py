class RebackNumber():
    def __init__(self,data:int) ->bool:
        self.data = data

    def reback(self):
        data_str = str(self.data)
        data_lis = list(data_str)
        reverse_data = "".join(reversed(data_lis))
        if reverse_data == data_str:
            return True
        else:
            return False

r = RebackNumber(-121)
print(r.reback())