import jaccard
import robotParser

a = "Test my. words of my project please"
b = "Test my words [of my project are] very important"

shinglesA = jaccard.createSet(jaccard.cleanUpString(a))
shinglesB = jaccard.createSet(jaccard.cleanUpString(b))

similarity = jaccard.compare(shinglesA, shinglesB)
print(similarity)



randArray = []


