import numpy as np
from numpy import linalg as LA
import scipy.linalg as sla
import numpy.random as rand

class TestCodes(object):
    def __init__(self):
        return
    def question1_rsquare(self, R):
        column_num = R.shape[1]
        res = None
        for col in range(column_num):
            if res is None:
                res = R * R[:, col]
                continue
            res = np.concatenate((res, R* R[:, col]), axis = 1)
        return res
    def question1(self):
        R = np.matrix([[1,2,3], [4,5,6] , [7,8,9]])
        print "R*R = {}".format(R*R)
        #column based calculation
        print "R*R = {}".format(self.question1_rsquare(R))
        
        
        return
    def question2(self):
        A = np.matrix([[1, 3, 2], [2,2,2] , [2,5,6]])
        x = np.matrix([0, -1, 0]).transpose()
        b = A * x
        print "b: {}".format(b)
        return
    def question3(self):
        A = np.matrix([[1, 1], [1, -1]])
        z_array = [2, 0, 1]
        
        for z in z_array:
            b = [6-3*z, 4-z]
            b = np.matrix(b).transpose()
            x = LA.solve(A, b)
            print "z= {}, x= {}, y = {}".format(z, x.item(0), x.item(1))
    def question4(self):
        P = np.matrix([[0, 1], [1, 0]])
        #here we suppose x = 3, y = 5, expect resul to be [5, 3]
        x = np.matrix([3, 5]).transpose() 
        
        print "Result: {}".format(P*x)
        print "P = {}".format(P)
             
        return
    def question5(self):
        P = np.matrix([[0, 1], [-1, 0]])
        #here we suppose x = 3, y = 5, expect resul to be [5, -3]
        x = np.matrix([3, 5]).transpose() 
        
        print "Result: {}".format(P*x)
        print "P = {}".format(P)
             
        return
    def question6(self):
        A = np.matrix([[1, 2], [3, 4]])
        b = np.matrix([1, 7]).transpose()
        x = LA.solve(A, b)
        print "x={}".format(x)
        return
    def question7(self):
        A = np.matrix([[2, 3], [10, 9]])
        x = np.matrix([2, -1]).transpose()
        b = A * x
        #b is expected to be [1,11]
        print "b: {}".format(b)
        return
    def question8(self):
        A = np.matrix([[3, 2], [6, 4]])
        b = np.matrix([10, 10]).transpose()
        x = LA.solve(A, b)
        print "x={}".format(x)
        return
    def question11(self):
        A = np.matrix([[1,2,3], [4,5,6] , [7,8,9]])
        E21 = np.matrix([[1,0,0], [-5,1,0] , [0,0,1]])
        #Expect it to be [[1,2,3], [-1,-5,-9] , [7,8,9]]
        print "E21*A = {}".format(E21*A)
        
        A = np.matrix([[1,2,3], [4,5,6] , [7,8,9]])
        E32 = np.matrix([[1,0,0], [0,1,0] , [0, 7, 1]])
        #Expect it to be [[1,0,0], [4,5,6] , [28,35,43]]
        print "E32*A = {}".format(E32*A)
        
        A = np.matrix([[1,2,3], [4,5,6] , [7,8,9]])
        P = np.matrix([[0,1,0], [0,0,1] , [1,0,0]])
        #Expect it to be [[4,5,6], [7,8,9] , [1,2,3]]
        print "P*A = {}".format(P*A)
        
        return
    def question12(self):
        A = np.matrix([[1,2,3], [4,5,6] , [7,8,9]])
        identity_matrix_transpose =  np.matrix([[0,0,1], [0,1,0] , [1,0,0]])
        #Expect it to be [[9,8,7], [6,5,4] , [3,2,1]]
        print "identity_matrix_transpose*A*identity_matrix_transpose = {}".format(identity_matrix_transpose*A*identity_matrix_transpose)
        
        A = np.matrix([[1,0,0], [-1,1,0] , [-1,0,1]])
        B = np.matrix([[1,2,3], [1,3,1] , [1,4,0]])
        #Expect it to the result to be [[1,2,3],[0,1,-2],[0,2,-3]]
        print "A*B = {}".format(A*B)
        return
    def question13(self):
        A = np.matrix([[2, 1], [3, 1]])
        b = np.matrix([5, 7]).transpose()
        x = LA.solve(A, b)
        print "m={}, c={}".format(x.item(0), x.item(1))
        return
    def question14(self):
        A = np.matrix([[1,0,0,0], [1,1,0,0], [1,2,1,0], [1,3,3,1]])
        E = np.matrix([[1,0,0,0], [-1,1,0,0], [0,-1,1,0], [0,0,-1,1]])
        # Expect A*E to be 
        print "E*A = {}".format(E*A)
        
        #get inverse of A
        M = LA.inv(A)
        print "M = {}".format(np.around(M))
      
        return
    def question16(self):
        A = np.reshape(rand.rand(9),(3,3))
        P, L, U = sla.lu(A)
        print "P= {}".format(np.around(P, decimals=2))
        print "L= {}".format(np.around(L, decimals=2))
        print "U= {}".format(np.around(U, decimals=2))
        return
    def run(self):
#         self.question1()

#         self.question2()
#         self.question3()
#         self.question4()
#         self.question5()
#         self.question6()
#         self.question7()
#         self.question8()
#         self.question11()
#         self.question12()
#         self.question13()
#         self.question14()
        self.question16()


        return
    
if __name__ == "__main__":   
    obj= TestCodes()
    obj.run()