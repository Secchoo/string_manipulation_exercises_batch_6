#use endwith() function without using endswith() function

def endswith(s, suffix):
    if len(suffix) == 0:
        return True
    if len(s) < len(suffix):
        return False
    return s[-len(suffix):] == suffix

print(endswith("hello world", "world"))  
print(endswith("hello world", "hello"))