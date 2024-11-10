# Given values
kilometers = 10
minutes = 43
seconds = 30
kilometers_in_mile = 1.61

# Convert time to total minutes
total_minutes =43.5

# Calculate average time per mile in minutes
average_time_per_mile = total_minutes / (10/kilometers_in_mile)

# Calculate average speed in miles per hour
average_speed_mph = kilometers/(43.5/60)/(10/kilometers_in_mile)

# Print the results
print(f"Average Time per Mile: {average_time_per_mile:.2f} minutes")
print(f"Average Speed: {average_speed_mph:.2f} mph")
