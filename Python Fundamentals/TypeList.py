# Filter by type

def filter():
    if isintance(val, str):
        if len(val) >= 50:
            print "Long sentence"
        else:
            print "Short sentence"
    elif: isintance(val, int):
        if val >= 100:
            print "That's a Big number!"
        else:
            print "That's a small number.."
    elif isintance(val, list):
        if len(val >= 10):
            print "Big list!"
        else:
            print "Short list.."
