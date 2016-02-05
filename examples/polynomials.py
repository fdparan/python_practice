class Polynomials:
    def __init__(self, coef):
        """constructor"""
        self.coefficient = [] + coef # shallow copy of coef

    def degree(self):
        """Highest power with a non-zero coeffiient"""
        return len(self.coefficient)

    def asList(self):
        """return a (shallow) copy of coefficient"""
        return [] + self.coefficient

    def __eq__(self, aPoly):
        """return self == aPoly"""
        print 'here'
        return self.coefficient == aPoly.asList()

    def __ne__(self, aPoly):
        """return self != aPoly.asList"""
        return self.coefficient != aPoly.asList()
    
    def __str__(self):
        """return string representation"""
        r = ""
        p = len(self.coefficient)
        print self.coefficient, p

        for i in range(len(self.coefficient)):

            if self.coefficient[i] > 0:

                '''
                implementation using if-else statements
                '''
                # term = ''
                #
                # if self.coefficient[i] > 1:
                #     term += str(self.coefficient[i])
                #
                # if i > 1:
                #     term += "x^" + str(i)
                # elif i == 1:
                #     term += "x"

                '''
                implementation using one-line, if-else statements
                (more concise & straightforward)
                '''
                term = "x" if self.coefficient[i] == 1 else str(self.coefficient[i]) + "x"
                term += "^" + str(i) if i > 1 else term.strip("x")

                r = term + r if i == len(self.coefficient)-1 else "+" + term + r

        # while p > 0:
        #     p = p - 1
        #     if self.coefficient[p] == 0: continue
        #     if p < len(self.coefficient) - 1: r = r + "+"
        #     r = r + str(self.coefficient[p])
        #     if p == 0: continue
        #     r = r + "x"
        #     if p <= 1: continue
        #     r = r + "^" + str(p)
            
        return r.strip("+")


def main():
    obj = Polynomials([0,3,0,1,5,2,0])
    print obj

if __name__ == '__main__':
    main()