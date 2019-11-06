def checkRecord( s):
    if  s.count('A') < 2 and  s.count('LLL') == 0:
        return True
    else :
        return False







if __name__ == '__main__':
    s = "PPALLL"
    print(checkRecord(s))