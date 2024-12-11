def build_lps_table(pattern):
    lps = [0] * len(pattern)
    length = 0  
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):

    lps = build_lps_table(pattern)
    matches = []

    i = 0
    j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

text = [1, 5, 2, 9, 6, 5, 2, 9, 8, 5, 2, 7]
pattern = [6, 5, 2]

print("Text:", text)
print("Pattern:", pattern)

matches = kmp_search(text, pattern)
print("Pattern found at indices:", matches)
