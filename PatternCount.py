# Code Challenge: Implement PatternCount (reproduced below).
#      Input: Strings Text and Pattern.
#      Output: Count(Text, Pattern).

#     PatternCount(Text, Pattern)
#         count ← 0
#         for i ← 0 to |Text| − |Pattern|
#             if Text(i, |Pattern|) = Pattern
#                 count ← count + 1
#         return count

# Sample Input:
# GCGCG
# GCG

# Sample Output:
# 2

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

if __name__== "__main__":
    pattern = "GCG"
    text = "GCGCG"

    v = PatternCount(pattern, text)
    print(v)