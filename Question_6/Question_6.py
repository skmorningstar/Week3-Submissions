while True:
  try:
    length=input()
    needle=input()
    haystack=input()
    if needle in haystack:
        for i in range (0,len(haystack)):
                if haystack[i:i+len(needle)]==needle:
                    print(i)
    else:
        print("\n")
 
  except EOFError: 
    break