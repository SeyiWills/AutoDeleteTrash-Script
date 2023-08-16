#import the required modules
import winshell
#import sched
import sched
#import time
import time


event_schedule = sched.scheduler(time.time, time.sleep)
#create a function to have the code runing

def auto_delete():
    #get all the files in the recycle bin and delete
    event_schedule.enter(30,1, auto_delete)


#us try and execept block to handle exceptions

    try:
    # Calling the built-in function to delete
    #the data inside Recycle-Bin
    
        winshell.recycle_bin().empty(confirm=False,
                                 show_progress = False, sound=True)
    
    #print status of deletion
        print("Recycle Bin has been emptied")
    except:
    
    #print the Recyle-Bin is already Empty!
        print ("The recycle bin is empty!")
    
event_schedule.enter(30,1, auto_delete)
event_schedule.run()