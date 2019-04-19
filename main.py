# Labor Of Love
# Created By David Hinojosa

import time
#import kivy

stored_time = []

#Open / Write time Keeper
open("myTime.txt", "w")

start = input("Press enter to start timer")

begin = time.time()

print("Timer has started")

endtime = input("Press enter to stop timer")

end = time.time()

print("Stopped Timer")

elapsed = end - begin

elapsed = int(elapsed)

print("Time passed is: ", elapsed)

stored_time.append(elapsed)

print("stored time", stored_time)