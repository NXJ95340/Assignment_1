import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("ages : ", ages)
#sorting age
ages.sort()
#printing the sorted list of ages
print("Sorted ages : ", ages)
#finding the minimum and maximum ages
minimum = min(ages)
maximum = max(ages)
print ("Minimum age: ",minimum, "and maximum age: ", maximum)
#adding the min age and max age to list
ages.append(minimum)
ages.append(maximum)
print("Ages: ",ages)
#finding the median of ages
median_age = statistics.median(ages)
print("Median:", median_age)
#finding the average of ages
sum_ages = sum(ages)
length = len(ages)
average = sum_ages/length
print("Average: ",average)
#range of ages
range = maximum - minimum
print("Range: ",range)






