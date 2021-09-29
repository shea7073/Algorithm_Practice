
def anagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    if len(s1) != len(s2):
        return False

    length = len(s1)

    for j in range(length):
        for i in range(length):
            if len(s1) == 0:
                break
            if s1[0] == s2[i]:
                s1 = s1.replace(s1[0], "")
                print(s1, s2)

    if len(s1) == 0:
        return True
    else:
        return False


print(anagram("hello", "hello"))