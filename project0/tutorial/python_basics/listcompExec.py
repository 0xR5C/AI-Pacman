ar = ['ONE', 'TWOOOOO', 'THREE', 'FOUR', 'FIVEEE']
lower = [x.lower() for x in ar if len(x)>5]
print(lower)