s = "hello class"
print(s.lstrip("h"))
print(s.center(150))
print(s.find("o", 0, 3))
print(s[3:-2:1])

s = s.lower()
vc = 0
cc = 0
vowel = 'aeiou'
for i in s:
    if i in vowel:
        vc += 1
    else:
        cc += 1
print(vc)
name = "khelvendra"
print(name[4::-1], name[-1:4:-1], sep="")


def anagram(name1, name2):
    if len(name1) != len(name2):
        return "not anagram"
    else:
        if sorted(name1) == sorted(name2):
            return "anagram"
        else:
            return "not anagram"


print(anagram("shiv", "shiv"))
