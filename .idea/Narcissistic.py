#水仙花数字  所有数字的立方和等于原数字
class Narcissistic():
    #传入起始值和终止值，返回起始值与终止值之间所有的水仙花数
    def __init__(self,start_num,stop_num):
        self.start_num = start_num
        self.stop_num = stop_num
        self.li = []
    def get_list(self):
        for vv in range(self.start_num, self.stop_num):
            print('vv is ', vv)
            num_list = list(str(vv))
            print("数字列表是：", num_list)
            sum = 0
            for val in num_list:
                sum = sum + int(val) * int(val) * int(val)
            print('当前水仙花计算值是：%s'%sum)
            if int(vv) == sum:
                self.li.append(sum)
        return(self.li)
            #print('水仙花值是：', sum)
            #print('符合水仙花的数字列表是:', sum_list)
n1 = Narcissistic(100,1001)
print(n1.get_list())
