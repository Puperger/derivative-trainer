from pick import pick

def Sum():
    title = 'Use Sum Rule?'
    options = ["Yes","No"]
    _, index = pick(options,title)
    return index

def Product():
    title = 'Use Product Rule?'
    options = ["Yes","No"]
    _, index = pick(options,title)
    return index

def Quot():
    title = 'Use Quotient Rule?'
    options = ["Yes","No"]
    _, index = pick(options,title)
    return index

