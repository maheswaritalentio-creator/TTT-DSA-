def anagram(s,t):
    l1=list(s)
    l2=list(t)
    l1.sort()
    l2.sort()
    if l1==l2:
        print("true")
    else:
        print("false")

t=int(input())
for i in range(t):
    s=input()
    t=input()
    anagram(s,t)

    
