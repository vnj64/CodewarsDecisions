def generate_hashtag(s):
    if len(s) != 0:
        if (len(s) < 140):
            result = '#'
            s = s.split(' ')
            for i in range(len(s)):
                s[i] = s[i].capitalize()
                result = result + s[i]
            return result
        else:
            return False
    else:
        return False

print(generate_hashtag(''))