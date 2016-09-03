import numpy as np
from numpy import linalg as LA

class Hw1(object):
    def __init__(self):
        return
    def question2(self):
        c = 2
        d = 4
        res = c * np.array([1,2]) + d * np.array([3,1])
        print res
        return
    def question5(self):
        r1 = [1.0/2, -1.0/2, -1.0/2, 1.0/2]
        print "r1 lenght {}".format( LA.norm(r1, ord=2))
        return
    def question7(self):
        u = np.array([1,2,3]).reshape((3,1))
        v = np.array([4,5,6]).reshape((3,1))
        w = np.array([7,8,9]).reshape((3,1))
        res = np.concatenate((u,v,w), axis = 1)
        print "column order {}".format(res) 
        
        res = np.concatenate((u.transpose(),v.transpose(),w.transpose()), axis = 0)
        print "row order {}".format(res)          
        return
    def question8(self):
        u0 = np.matrix([1,0]).transpose()
        A = np.matrix([[0.8, 0.3], [0.2, 0.7]])
        res = [u0]
        for i in np.arange(1,4,1):
            temp = A * res[i-1]
            res.append(temp)
            print "u{} {}".format(i, temp)
        return
    def question9(self, u0):
        A = np.matrix([[0.8, 0.3], [0.2, 0.7]])
        res = [u0]
        for i in np.arange(1,20,1):
            temp = A * res[i-1]
            res.append(temp)
            print "u{} {}".format(i, temp)
        return
    def question10(self):
        identtity_matrix = np.matrix([[1.0, 0.0], [0.0, 1.0]])
        A = np.matrix([[0.8, 0.3], [0.2, 0.7]])
        A = A - identtity_matrix
        b = np.matrix([0.0, 0.0]).transpose()
        u = LA.solve(A, b)
        print "stable u {}".format(u)
        return
    def run(self):
#         self.question2()
#         self.question5()
#         self.question7()
#         self.question8()
        u0 = np.matrix([1,0]).transpose()
        self.question9(u0)
        self.question10()
        u0 = np.matrix([0,0]).transpose()
        self.question9(u0)
        return
    
if __name__ == "__main__":   
    obj= Hw1()
    obj.run()