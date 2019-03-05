# FrequentWords(Text, k)
#     FrequentPatterns ← an empty set
#     for i ← 0 to |Text| − k
#         Pattern ← the k-mer Text(i, k)
#         Count(i) ← PatternCount(Text, Pattern)
#     maxCount ← maximum value in array Count
#     for i ← 0 to |Text| − k
#         if Count(i) = maxCount
#             add Text(i, k) to FrequentPatterns
#     remove duplicates from FrequentPatterns
#     return FrequentPatterns

from PatternCount import PatternCount
from Utils import removeDuplicates, printItems

def FrequentWords(Text, k):
    FrequentPattern = []

    Count = {}
    for i in range(len(Text) - k):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    maxCount = max(Count.values())
    for i in range(len(Text) - k):
        if Count[i] == maxCount:
            FrequentPattern.append(Text[i:i+k])
    return removeDuplicates(FrequentPattern)

if __name__== "__main__":
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    output = FrequentWords(text, k)

    printItems(output)
