language=' python '
print(language)#有空白
print(language.strip())#仅在本次输出中删除空白

language=language.strip()#对变量本身进行修改则可以永久改变language的字符，即去掉了空格
print(language)
