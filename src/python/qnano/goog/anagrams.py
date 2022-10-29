
def anagrams(S):

    for s in S:
        A, B = s.split(" ")
        anagrams_indices = set()
        b_sorted = sorted(B)

        for i in range(0, len(A)-len(B)):
            if sorted(A[i:i+len(B)]) == b_sorted:
                anagrams_indices.add(i)

        print(len(anagrams_indices), anagrams_indices)

S = ["abdcghbaabcdij bcda", "bbbababaaabbbb ab"]

anagrams(S)


