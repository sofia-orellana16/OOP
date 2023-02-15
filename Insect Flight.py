import InsectClass as I
# name of python file - not name of class

# The main function.
def main():
       mosquito = I.Insect('mosquito',2,4) 
       housefly = I.Insect('housefly',2,4)                            # this creates an instance called 'my_coin' of the class 'Coin()'
# has to match name of the class
       
       mosquito.flight_length()
       housefly.flight_length() 
       
       print('the {mosquito.get_name()} can fly up to {mosquito.get_flighttime()}')                            # notice you do not have to supply the argument/parameter
       print('the {mosquito.get_name()} can fly up to {housefly.getflighttime()}')

    
           
           
       

           


       

# Call the main function.

main()
