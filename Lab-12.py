lst=[]
def filter_long_words(lst,integer):
    word_len = []
    for n in lst:
        if len(n)>integer:
          word_len.append((len(n), n))
    word_len.sort()
    return word_len

integer=int(input("enter number"))

n=int(input("Enter number of elements "))
for i in  range(0,n):
    ele=str(input())
    lst.append(ele)


print( filter_long_words(lst,integer))

