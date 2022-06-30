def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs['first'])
  
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")