str1 = "The quick brown fox jumps over the lazy dog."
print(str1)
words = input("enter word : ")
result = "result : {}"
print(result.format(str1.lower().count(words.lower())))