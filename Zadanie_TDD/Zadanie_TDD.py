

class mat(object):
    def min(self, arg1,arg2):
        return arg1 if arg1<arg2 else arg2

    def max(self, arg1,arg2):
        return arg2 if arg1<arg2 else arg1

    def ispositive(self, arg1,arg2):
        return -arg1 if arg1<0 else arg1
