import random
class TravelingSales():
    def __init__(self):
        self.is_random = input("Do you want this to be a randomly generated problem or not? Y or N ")
        if self.is_random in ["Yes","y","Yes","Y"]:
            self.num_cities = int(round(random.uniform(2,20),0))
            self.base = int(round(random.uniform(2,self.num_cities),0))
            self.destin = int(round(random.uniform(2,self.num_cities),0))
            self.time = int(round(random.uniform(2,20),0))
            self.createRandomTravelCost(self.num_cities)
            self.mirrorCost()
            self.rev = []
            for i in range(self.num_cities):
                self.rev.append(round(random.uniform(0,100),0))            
        else:
            self.customInputs()
            self.rev = []
            for i in range(len(self.rev_dict)):
                self.rev.append(self.rev_dict[i][1])
        #rev is the benefit matrix where cost is the travel cost matrix
    def mirrorCost(self):
        for row in range(len(self.cost)):
            for col in range(len(self.cost[row])):
                if self.cost[row][col] != 0:
                    self.cost[col][row] = self.cost[row][col]
    def createRandomTravelCost(self,num_cities):
        self.cost = []
        for i in range(num_cities):
            temp = []
            for k in range(num_cities):
                temp.append(0)
            self.cost.append(temp)
        for row in range(len(self.cost)):
            for col in range(row):
                if row == col:
                    continue
                else:
                    self.cost[row][col] = round(random.uniform(1,100),0)
    #need to fill second half by mirror
    def ToIndex(self,city_name):
        out = 0
        for i in range(len(self.rev_dict)):
            if self.rev_dict[i][0] == city_name:
                out = i
                break
        return out
    def ToName(self,index):
        return self.rev_dict[index][0]
    def customInputs(self):
            #code for custom travel cost matrix creation
        self.num_cities = eval(input("Please enter the number of cities : "))
        self.rev_dict = []
        for i in range (self.num_cities):
            temp = []
            city_name = input("Please enter City " + str(i+1) + "'s Name : ")
            rev = eval(input("Please enter " + city_name + "'s associated revenue "))
            temp.append(city_name)
            temp.append(rev)
            self.rev_dict.append(temp)
        self.starting_city = input("Which city is the salesperson beginning at? ")
        self.ending_city = input("Which city is the salesperson ending at? ")
        self.base = self.ToIndex(self.starting_city)
        self.destin = self.ToIndex(self.ending_city)
        self.time = eval(input("How many days can the salesperson travel? "))
    #input travel costs
        self.cost = []
        for i in range(self.num_cities):
            temp = []
            for k in range(self.num_cities):
                temp.append(0)
            self.cost.append(temp)
        for row in range(len(self.cost)):
            for col in range(row):
                if row == col:
                    continue
                else:
                    self.cost[row][col] = eval(input("Travel Cost from " + self.rev_dict[row][0] + ' to ' + self.rev_dict[col][0] + ' : '))
        self.mirrorCost()
    def createEmpty2d(self):
        out = []
        for i in range(self.num_cities):
           temp = []
           for k in range(self.time +2):
                temp.append("na")
           out.append(temp)
        return out
    def __str__(self):
        #print shortest path -
        short = []
        t = 0
        previous = None
        while t < self.time + 2:
            if t == 0:
                short.append(self.base)
            else:
                short.append(self.next_city[self.next_city[previous][t-1]][t])
            previous = (short[-1])
            t += 1
        #format printing
        out = ""
        for i in range (len(self.cost)):
            if i == 0:
                out += "With a cost matrix of: " + str(self.cost[i]) + '\n'
            else:
                out += "                       " + str(self.cost[i]) + '\n'
        out += '\n'
        out += 'And revenue matrix of: ' + str(self.rev) + '\n'
        if self.is_random in ["Yes","y","Yes","Y"]:
            out += 'Starting at City ' + str(self.base) + ' And Ending at City ' + str(self.destin) + '\n' + 'The optimal path is : \n'
            for i in range(self.time+1):
                if i == 0:
                    out += 'Begin at City ' + str(short[i]) + '\n'
                else:
                    out += 'At t = ' +  str(i) + ', be at ' + str(short[i]) + '\n'
        else:
            out += 'Starting at ' + self.starting_city + ' And Ending at ' + self.ending_city + '\n The optimal path is: '
            for i in range (self.time + 1):
                if i == 0:
                    out += 'Begin at ' + str(self.ToName(short[i])) + '\n'
                else:
                    out += 'At t = ' + str(i) + ', be at ' + str(self.ToName(short[i])) + '\n'
        for k in range(len(self.values)):
            if type(self.values[k][0]) == int:
                out += 'The profit from this path is ' + str(self.values[k][0])
        return out
    def solve(self):
        #self.destin = destination
        #self.base = starting point
        sValues = []
        tValues = []
        for i in range(0,self.num_cities):
            sValues.append(i)
        for k in range(self.time+2):
            tValues.append(k)
        self.values = self.createEmpty2d()
        self.next_city = self.createEmpty2d()
        for ti in range(len(tValues)-1,-1,-1):
            for si in range(len(sValues)):
                if ti == len(tValues)-1:
                    self.values[si][ti] = 0
                    self.next_city[si][ti] = "END"
                elif ti == len(tValues) - 2:
                    self.values[si][ti] = self.rev[si] - self.cost[si][self.destin] 
                    self.next_city[si][ti] = self.destin
                elif ti == 0:
                    if si == self.base:
                        max_matrix = []
                        for i in range(self.num_cities):
                            max_matrix.append(self.values[i][1] - self.cost[self.base][i])
                            #find max at ti = 1
                        self.values[si][ti] = max(max_matrix)
                        next_cit = [i for i,j in enumerate(max_matrix) if j == self.values[si][ti]][0]
                        self.next_city[si][ti] = next_cit
                    else:
                        self.values[si][ti] = 'N'
                        self.next_city[si][ti] = 'N'
                else:
                    #loop through city list
                    max_matrix = []
                    for i in range(self.num_cities):
                        max_matrix.append(self.rev[i] - self.cost[si][i] + self.values[i][ti + 1])
                    self.values[si][ti] = max(max_matrix)
                    self.next_city[si][ti] = [i for i,j in enumerate(max_matrix) if j == self.values[si][ti]][0]
        print(self)
        printMat(self.values)
        print()
        printMat(self.next_city)
    def solve_every(self,every_city):
        #would you just have a cities already traveled matrix?
        print('ell0')
def printMat(matrix):
    #matrix is a 2d list
    out = ""
    for k in range(len(matrix)):
        out += str(matrix[k])
        out += "\n"
    print (out)
def main():
    #iterate backwards
    test = TravelingSales()
    test.solve()
    k = raw_input()
main()
