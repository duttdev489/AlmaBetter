s = input()
def check_palindromes( str_s):
  if str_s==str_s[::-1]:
    return True
  else:
    return False
res= check_palindromes( s)
print(res)
