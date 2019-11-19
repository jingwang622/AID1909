import re
def find_address(port_name):
    regex1 = re.compile(r'[^(Internet)] address is ([a-f|0-9]{1,4}.){2}([a-f|0-9]{1,4})(.[a-f|0-9]{1,4})?')
    regex2 = re.compile(r'Internet address is ([0-9]{1,3}.){3}([0-9]{1,3})?')
    fr = open("exc.txt","r")
    content = fr.read()
    content_list = content.split("\n\n")
    content_list.remove(content_list[0])
    for item in content_list:
        value_list = item.split(" ",1)
        if value_list[0] == port_name:
            try:
                value1 = regex1.search(value_list[1]).group()
                print(value1)
            except Exception as e:
                print("address is Unknown")
            try:
                value2 = regex2.search(value_list[1]).group()
                print(value2)
            except Exception as e:
                print("Internet address is Unknown")




if __name__ == '__main__':
    while True:
        port_name = input("请输入一个端口：")
        find_address(port_name)