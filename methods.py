class agent:

    def _init_(self,name,age,health):
        print('Welcome to the Game')
        self.name=name
        self.age=age
        self.health=100
        self.alive=true
      
    def curr_health(self):
       
        print("current health of",self.name,"is",self.health)
        print("run!")

    def punched(self):
        self.health-=10

    def shooted(self):
        self.health-=50

    def is_alive(self):
        if self.health==0:    
            alive=False

    def info(self):
        print("Name  : ",self.name)
        print("Age  : ",self.age)
        print("Health :",self.health)
            




    
p1=agent("Aryan",20)
p1.curr_health()

p1.punched()
p1.shooted()
p1.info()
print('-'*45)

