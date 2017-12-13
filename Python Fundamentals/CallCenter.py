# You're creating a program for a call center. Every time a call comes in you need a way to track that call.//
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.//
# You will create two classes. One class should be Call, the other CallCenter.//
class Call(object):
    def __init__(self, unique_id, caller_name, phone_number, time, reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def displayAll(self):
        print self.unique_id
        print self.caller_name
        print self.phone_number
        print self.time
        print self.reason

caller1 = Call("001", "Kanye West", "808-303-4400", "17:38", "Complaint about Taylor Swift")
caller2 = Call("002", "Taylor Swift", "754-302-4414", "17:67", "Complaint about Kanye West")
caller3 = Call("003", "OJ Simpson", "954-343-2223", "18:01", "Wondering why cops are follwing him..")
caller4 = Call("004", "Tiger Woods", "754-232-4114", "18:30", "Broken back")
caller5 = Call("005", "Carson Daly", "212-213-2232", "18:57", "Wants TRL back, ASAP!")
caller6 = Call("006", "Donald Trump", "212-234-4334", "19:21", "Can't figure out why everyone hates him")    

# caller6.displayAll()   

class callCenter(object): 
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self,caller):
        self.calls.append(caller)
        self.queue_size += 1
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        for element in self.calls:
            print element.caller_name, element.phone_number
            # print self.calls[1].caller_name
            print self.queue_size
            return self

test_calls = callCenter()
test_calls.add(caller2).add(caller4).add(caller1).add(caller3).remove().info()