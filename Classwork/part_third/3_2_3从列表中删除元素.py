motor=['honda','yamaba','suzuki']

del motor[0]
print(motor)

#使用pop()方法删除元素
#若想删除任意位置的元素，在括号内添加索引即可pop(0)
popped_motor=motor.pop()#从末尾删除了一个元素
print(motor)#打印删除了元素之后的内容
print(popped_motor)#打印所被删除的元素

#注意所被输出的空格位置
print(f"the bike is sold is{ popped_motor.title() }")#the bike is sold isSuzuki
print(f"the bike is sold is {popped_motor.title()}")#the bike is sold is Suzuki

#根据值删除元素，remove()方法删除元素
moto=['honda','yamaba','suzuki']
tooexpensive='yamaba'
moto.remove(tooexpensive)
print(moto)
print(f"\n the {tooexpensive.title()} is too expensive for me")
#使用remove删除其值后，也可继续使用他的值


