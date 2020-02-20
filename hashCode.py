import statistics

class Library:
    def __init__(self, N, T, M, ids, mean, days):
        self.books = N
        self.signup = T
        self.rate = M
        self.bookIDs = [int(i) for i in ids]
        self.mean = mean
        self.score = M * mean * (days - T)

    def printDetails(self):
        print("Books : ", self.books, "Signup time : ", self.signup, "Rate : ", self.rate, "Score = ", self.score)
        print("Book ids : ")
        for i in self.bookIDs:
            print(i, end=" ")
        print("")


class Solver:    
    def __init__(self, B, L, D, scores):
        self.days = D
        self.books = B
        self.libraries = L
        self.bookScores = [int(i) for i in scores]
        self.libraryList = []

    def printScores(self):
        print("Books : ", self.books, "Libraries : ", self.libraries, "Days : ", self.days)
        print("Book Scores : ")
        for i in self.bookScores:
            print(i, end=" ")
        print ("")
    
    def addLibrary(self, library):
        self.libraryList.append(library)

    def printLibraryDetails(self):
        id = 0
        print("=========== Library Details ============")
        for i in self.libraryList:
            print("Library id = " , id)
            i.printDetails()
            id = id+1
        print("")
    



input = "./inputs/a_example.txt"
inputFile = open(input)

line1 = inputFile.readline()
arr1 = line1.split(" ")
arr1 = [int(i) for i in arr1]
line2 = inputFile.readline()
scores = line2.split(" ")
solution = Solver(arr1[0],arr1[1],arr1[2],scores)
solution.printScores()
for i in range(arr1[1]):
    libStats = inputFile.readline()
    libstats = [int(i) for i in libStats.split(" ")]

    ids = inputFile.readline()
    books = ids.split(" ")
    books = [int(i) for i in books]

    costs = [solution.bookScores[i] for i in books]
    average = statistics.mean(costs)

    newLibrary = Library(libstats[0], libstats[1], libstats[2], books, average, solution.days)

    solution.addLibrary(newLibrary)

solution.printLibraryDetails()



