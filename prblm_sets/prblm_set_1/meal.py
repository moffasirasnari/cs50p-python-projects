#Meal time predictor
def main():
      users_ans= input("What time is it? ")
      time=convert(users_ans)

      if time >= 7 and time <= 8:
           print("breakfast time")
      elif time >=12 and time <= 13:
           print("lunch time")

      elif time >=18 and time<= 19:
           print("dinner time")
      else: print()



def convert(time):

     x , y =time.split(":") #time in format like 8:34
     y = float(y) / 60      #convert min in hr
     return float(x) + y    # will return float value to convert(user_ans)


if __name__ == "__main__": #pata ni kya hai, said will learn abt it later
    main()
