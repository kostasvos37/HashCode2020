import statistics

class Library:
    def __init__(self, N, T, M, ids, mean, days, libid):
        self.id = libid
        self.books = N
        self.signup = T
        self.rate = M
        self.bookIDs = [int(i) for i in ids]
        self.mean = mean
        self.score = M * mean * (days - T)

    def updateScore(self, R):
        self.score = self.rate * self.mean * (R - self.signup)

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
        self.remaining = D
        self.chosen = []

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

    def updateMetric(self):
        for library in self.libraryList:
            library.updateScore(self.remaining)

    def chooseLibrary(self):
        self.libraryList = sorted(self.libraryList, key = lambda i:i.score, reverse = True)
        if self.libraryList[0].signup < self.remaining:
            self.chosen.append((self.libraryList[0], self.days - self.remaining))
            first = self.libraryList.pop(0)
            self.remaining = self.remaining - first.signup
            self.updateMetric()
        else:
            self.libraryList.pop(0)
    
    def driver(self):
        while(self.libraryList):
            self.chooseLibrary()
    
    def results(self):
        print("\n ================ Results =================")
        for i in self.chosen:
            print("Library = ", i[0].id, "Signup time = ", i[1])
        


    
input = "./inputs/b_read_on.txt"
inputFile = open(input)

line1 = inputFile.readline()
arr1 = line1.split(" ")
arr1 = [int(i) for i in arr1]
line2 = inputFile.readline()
scores = line2.split(" ")
solution = Solver(arr1[0],arr1[1],arr1[2],scores)
#solution.printScores()

counter = 0
for i in range(arr1[1]):
    libStats = inputFile.readline()
    libstats = [int(i) for i in libStats.split(" ")]

    ids = inputFile.readline()
    books = ids.split(" ")
    books = [int(i) for i in books]

    costs = [solution.bookScores[i] for i in books]
    average = statistics.mean(costs)

    newLibrary = Library(libstats[0], libstats[1], libstats[2], books, average, solution.days, counter)
    counter = counter + 1
    solution.addLibrary(newLibrary)

#solution.printLibraryDetails()

solution.driver()
solution.results()

