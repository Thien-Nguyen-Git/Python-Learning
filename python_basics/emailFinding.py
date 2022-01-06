# Vikram solution

# break example
# myFile=open('emails.txt','r')
# # print(myFile.read())
# emailList=myFile.read()
# emails=emailList.split(",")
# print(emails)
# for email in emails:
#     if(email=="dev@gmail.com"):
#         print("email found")
#         break;


# continue example
numbers=[2,4,3,11,8]
for i in numbers:
    print('currewnt number is ',i)
    if i > 10:
        continue
    square = i * i
    print('square of i is ',square)


# find output
n = 7
c = 0
while(n):
    if(n>5):
        c=c+n-1
        n=n-1
    else:
        break
print(n)
print(c)