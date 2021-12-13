def lengthOfLastWord(s):
        newStr = s.split()

        if len(newStr) == 0:
        	print(0)

        else:
        	print(len(newStr[len(newStr)-1]))



test1 = "Hello World" #expected answer is 5
test2 = " " #expected answer is 0
test3 = "  Hi   my name is Kassandra    " # expected answer is 9

print(lengthOfLastWord(test1))
print(lengthOfLastWord(test2))
print(lengthOfLastWord(test3))

