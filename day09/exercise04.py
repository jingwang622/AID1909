import re
def find_address(port_name):
    fr = open("exc.txt",'r')
    while True:
        data = ""
        for line in fr:
            if line == "\n":
                break
            data += line
        if not data:
            return "该端口不存在"
        if port_name == re.match("\S+",data).group():
            regex1 = re.compile(r'[^(Internet)] address is ([a-f0-9]{1,4}.){2}([a-f0-9]{1,4})(.[a-f0-9]{1,4})?')
            regex2 = re.compile(r'Internet address is ([0-9]{1,3}.){3}([0-9]{1,3})?')
            try:
                value1 = regex1.search(data).group()
            except Exception as e:
                value1 = "address is Unknown"
            try:
                value2 = regex2.search(data).group()
            except Exception as e:
                value2 = "Internet address is Unknown"
            return (value1,value2)



if __name__ == '__main__':
    while True:
        port_name = input("请输入一个端口：")
        print(find_address(port_name))