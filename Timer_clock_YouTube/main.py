from playsound import playsound
import time

## ANSI Escape Sequence
YELLOW = '\033[33m'
RESET = '\033[0m'
RED = '\033[31m'
CLEAR = '\033[2J'
RETURN_HOME = '\033[H' 


## Now Take The Valid INPUT
#This function takes valid values of min and second within a range of 0 to 60
def valid_input_within_a_range(min_value,max_value,parameter):
    while True:
        user_input = int(input(f"Enter {parameter}: "))
        if user_input >= min_value and user_input <= max_value:
            return user_input
        else:
            print(f"{RED}Enter Valid Input!! TRY AGAIN{RESET}") 

# {RED} display content in red color in terminal
# {RESET} remove all the formatting


## Now Defining the Alarm function and main component of the project
def Alarm(total_time_in_sec):
    
    print(CLEAR) # {CLEAR} Cleans all the content from the terminal
    while (total_time_in_sec != -1):
        time.sleep(1) # waiting 1 sec
        hour_left = total_time_in_sec//3600         #Time left in hours
        min_left = (total_time_in_sec%3600)//60     #Time left in minutes
        sec_left = (total_time_in_sec%3600)%60      #time left in seconds

        ## // used to give the answer in integer value

        print(f"{CLEAR}{RETURN_HOME}{hour_left:02d}h {min_left:02d}m {sec_left:02d}s")  # This will shows the amount of time left till the alarm rings

        ##[:02d] this print decimal no. in 2 digit format and the no. is in 1 digit then this padd zero[0] at the starting
        ## {RETURN_HOME} returns the cursor to the starting of terminal

        total_time_in_sec -= 1   #reducing time by 1 second

    playsound("alarm.mp3") #this actually play sound in the terminal and keep the alarm name same in the parameter given to this function

def main():
    print(f"Input in form of {YELLOW}hh:mm:ss{RESET} ")
    hour = int(input("Enter Hour: "))                   
    min = valid_input_within_a_range(0,60,"Minutes")
    sec  = valid_input_within_a_range(0,60,"Second")


    ## Now we will calculate total time in second
    total_time_in_sec = (hour*60*60) + (min*60) + sec


    #time.sleep(1)
    ## Now Calling the Alarm function 
    Alarm(total_time_in_sec)

# Program execution Starts from here
if __name__ == "__main__":
    main()



# So this is the basic Timer/Alarm for beginner in python 
## Here in this we can do some basic editing and can enhance the code and output 