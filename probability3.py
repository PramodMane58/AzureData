totalcard = 52
totalace = 4
totalking = 3
totalafterking = 51
result = lambda x,y,a,b : (x/y *  a/b)*100

print(result(totalace,totalcard,totalking,totalafterking).__round__(2))