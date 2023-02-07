def is_polindrom(s):
    if s == "".join(reversed(s)):
        return True
    return False

a = input()

if is_polindrom(a) == True:
    print("Yes it is polindrom")
else:
    print("No it is not polindrom")