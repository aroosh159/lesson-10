class robot:
     Name = "Manufacturing Robot"
     function = "manufacture."
     inventer = "George Devol "
     inventingyear = "1967"
     def introduction(self):
       print("Hello I am a Robot.")
     def details(self):
        print("My name is ",self.Name)
        print("My function is to",self.function)
        print("I was first invented by ",self.inventer)
        print("I was invented in",self.inventingyear)
ob=robot()
ob.introduction()
ob.details()