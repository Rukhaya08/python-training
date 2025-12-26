'''Q)You are given two strings A and B.
Your task is to find and return a string representing the leftover string in A after removing all the letters that exist in string B.
Return "empty" if the output does not contain any value.
Note:
1)strings A and B contains alphabets in upper case only.
2)A single alphabet in B can replace all the occurence of that alphabet in A.  '''

def leftover(a,b):
    left=""
    remove=set(b)
    for ch in a:
        if ch not in remove:
            left+=ch
    if left:
        print(left)
    else:
        print("empty")
a="abcdef"
b="bde"
leftover(a,b)
