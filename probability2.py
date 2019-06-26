#drawing an ace after drawing a king on the first draw
totalcard = 52
totalace = 4
totalking = 4
totalafterking = 51
result = lambda x,y,a,b : (x/y) *  (a/b)

print(result(totalace,totalcard,totalking,totalafterking).__round__(2))
