distinguished_guest=['kyrie','curry','lebron','yaoming','morant']

#3-4打印邀请这些人来共进晚餐
print(f"i will invite {distinguished_guest} to dinner")

#3-5 修改嘉宾名单
  #3-5-1输出哪位嘉宾无法赴约
print(f"{distinguished_guest[4]} can't come to dinner")#python中语句不可被意外缩进
  #3-5-2将无法赴约的名单修改为被新邀请的名单
distinguished_guest[4]='james'
print(f"i will invite {distinguished_guest} to dinner")

#3-6添加嘉宾
  #3-6-1添加嘉宾到开头
distinguished_guest.insert(0,'spiderman')
  #3-6-2添加嘉宾到中间
distinguished_guest.insert(2,'wade')
  #3-6-3添加嘉宾到结尾
distinguished_guest.append('kobe')
print(f"i will invite {distinguished_guest} to dinner")

#3-7缩短名单
  #3-7-1打印只能邀请两个嘉宾共进晚餐
print("only two can join me for dinner")
  #3-7-2使用pop不断的删除嘉宾名单直到只有两位嘉宾为止并每次弹出以为嘉宾都打印抱歉信息
while len(distinguished_guest)>2:
    print(f"sorry {distinguished_guest.pop()} i can't invite you to dinner")
    #pop内不加任何参数时，是从末尾开始删除名单信息
  #3-7-3对于余下的两个嘉宾，打印消息指出其仍在受邀之列
print(f"{distinguished_guest[0]} and {distinguished_guest[1]} are still invited")
  #3-7-4使用del将最后两名嘉宾删除，让名单变成空的并打印验证
while len(distinguished_guest)>0:
    del distinguished_guest[0]

#检验是否为空，若不为空，则输出distinguished_guest的列表元素值
if len(distinguished_guest)==0:
    print(f"the list is empty")
else:
    print(f"{distinguished_guest}")
