def split_and_join(line):
    # write your code here
    line=input()
    z=line.split(line)
    print(z)
    b="-".join(z)
    print(b)
    
    
    if __name__='__main__':
      line=input()
      result=split_and_join(line)
      print(result)
