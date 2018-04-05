# Name: Vinson Aiono
# Date: 4/3/2018
# Coding Dojo Python Stack
# Description: Create two classes. one call and one callcenters

class Call:
    def __init__(self, uniqueId, name, phoneNum, timeOfCall, reasonForCall):
        self.uniqueId = uniqueId
        self.name = name
        self.phoneNum = phoneNum
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall
        
        # self.Display()
        return

    def Display(self):
        print('Unique ID:', self.uniqueId)
        print('Name:', self.name) 
        print('Phone Number:', self.phoneNum)
        print('Time of call:', self.timeOfCall)
        print('Reason for call:', self.reasonForCall)
        print('--------------------------------------')

class CallCenter:
    def __init__(self):
        self.callLog = []
        self.queSize = 0
        return 
    # Adds calls to the Que
    def add(self, call):
        self.callLog.append(call)
        self.queSize += 1
        self.info()
        return self
    # Removes calls from Que
    def remove(self, call):
        for x in range(1, len(self.callLog)):
            self.callLog[x-1] = self.callLog[x]
        self.callLog.pop()
    # display info
    def info(self):
        print('Calls in Que', len(self.callLog))
        for x in range(0, len(self.callLog)):
            print("Name:", self.callLog[x].name, 'Phone:', self.callLog[x].phoneNum)
        return self
            


caller1 = Call(1, 'john smith', 5555555555, 3, 'complaint')
caller2 = Call(2, 'James Johnson', 5555555555, 3, 'compliment')
caller3 = Call(3, 'George Washington', 5555555555, 3, 'conlaint')

callcenterSanjose = CallCenter()

callcenterSanjose.add(caller1).add(caller2).add(caller3)