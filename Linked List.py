class Node:
    def __init__(self,Roll_Number,Year,Semester,Email):
        self._Roll_Number = Roll_Number
        self._Year = Year
        self._Semester = Semester
        self._Email = Email
        self.next = None
    def display(self):
        print("Student Data is: ", self._Roll_Number,self._Year,self._Semester,self._Email)
    def getData(self):
        return self._Roll_Number    
class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def Add_Start(self,data):
        if self.head == None:
            self.head = data
            self.size = self.size + 1
        else:
            data.next = self.head
            self.head = data
            self.size = self.size + 1
        
    def Add_End(self,data):
        if self.head == None:
            self.head = data
            self.size = self.size + 1 
            return
        else:
            Temp = self.head
            while Temp.next != None:
                Temp = Temp.next
            Temp.next = data
            self.size = self.size + 1
    
    def Add_AnyPosition(self,Index,data):
        if Index == 0:
            self.Add_Start(data)
            return
        elif Index == self.size:
            self.Add_End(data)
            return
        current = self.head
        for i in range(Index-1):
            current = current.next
        data.next = current.next
        current.next = data
    
    def Delete_Start(self):
        if self.head == None:
            print("Your Linked List is empty")
            return
        self.head = self.head.next
        self.size = self.size - 1
    
    def Delete_End(self):
        if self.head == None:
            print("Your Linked is empty")
            return
        current = self.head
        while current.next.next != None:
            current = current.next
        current.next = None
        self.size = self.size - 1
    
    def Delete_AnyPosition(self,Index):
        if Index == 0:
            self.Delete_Start()
            return
        elif Index == self.size-1:
            self.Delete_End()
            return
        current = self.head
        for i in range(Index-2):
            current = current.next
        current.next = current.next.next
    
    def Search_RollNumber(self,Roll_Number):
        current = self.head
        found = False
        while (current != None):
            if(current.getData() == Roll_Number):
                found = True
                break
            current = current.next
        if(found):
            print("Roll Number is in the List")
        else:
            print("Roll Number is not in the List")
            
    def Reverse(self,head):
        if head != None:
            self.Reverse(head.next)
            head.display()
    def Print_Reverse(self):
        self.Reverse(self.head)

    def Display_Values(self):
        current = self.head
        while(current != None):
            current.display()
            current = current.next
              
    def Display(self):
        Do = input("Please Press S to start the program: ")
        while Do != "i":
            Choice = input("Enter your choice from a,b,c,d,e,f,g,h,i please: ")
            if Choice == 'a':
                loop = int(input("how many times you want to enter data: "))
                for i in range(loop):
                    Roll_Number = int(input("Enter your Roll Number Please: "))
                    Year = int(input("Enter your Year Please: "))
                    Semester = input("Enter your Semester Please: ")
                    Email = input("Enter your Email Please: ")
                    List.Add_Start(Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'b':
                Index = int(input("Enter position to add Node: "))
                Roll_Number = int(input("Enter your Roll Number Please: "))
                Year = int(input("Enter your Year Please: "))
                Semester = input("Enter your Semester Please: ")
                Email = input("Enter your Email Please: ")
                List.Add_AnyPosition(Index,Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'c':
                Roll_Number = int(input("Enter your Roll Number Please: "))
                Year = int(input("Enter your Year Please: "))
                Semester = input("Enter your Semester Please: ")
                Email = input("Enter your Email Please: ")
                List.Add_End(Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'd':
                List.Delete_Start() 
                List.Display_Values()      
            if Choice == 'e':
                Index = int(input("Enter your Index from where you want to delete: "))
                List.Delete_AnyPosition(Index)
                List.Display_Values()
            if Choice == 'f':
                List.Delete_End()
                List.Display_Values()
            if Choice == 'g':
                Roll_Number = int(input("Enter your Roll Number Please: "))
                List.Search_RollNumber(Roll_Number) 
            if Choice == 'h':
                List.Display_Values()
            if Choice == 'i':
                List.Print_Reverse()
            if Choice == 'j':
                print("Invalid Command")
                break
               
List = Linked_List()
List.Display()

    