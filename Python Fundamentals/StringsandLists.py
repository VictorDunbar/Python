# find and replace

words = "It's thanksgiving day. It's my birthday, too!"
dayposition = words.find("day")
print dayposition
newstr = words.replace("day", "month")
print newstr

# min and max

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

# first and last

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[len(x)-1]
y = []
y.append(x[0])
y.append(x[len(x)-1])
print y

# New list

x = ["hello", 2, 3, 4, 5, 6, "world"]
x.sort()
print x
y = x[:len(x)/2]
z = x[len(x)/2:]
print y
print z
y.append(z)
print y
