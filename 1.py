s=input("Enter a string=")
arr=[0]*26
for i in range(len(s)):
    arr[ord(s[i])-97]+=1
for i in range(len(arr)):
    if(arr[i] > 0):
        print(chr(i+97),"->",arr[i])