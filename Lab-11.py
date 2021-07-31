lst=[]
def longest_word(lst):
    word_len = []
    for n in lst:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

n=int(input("Enter number of elements "))
for i in  range(0,n):
    ele=str(input())
    lst.append(ele)


result = longest_word(lst)
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
