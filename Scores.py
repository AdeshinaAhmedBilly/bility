total_score = 0.0  
highest_score = 0.0  
lowest_score = 100.0 

for i in range(1, 11):
    score = float(input(f"Enter the score for student {i}: "))  
    
    total_score += score 
    
    if score > highest_score:
        highest_score = score  
    
    if score < lowest_score:
        lowest_score = score  

average_score = total_score / 10
range_of_scores = highest_score - lowest_score

print("\nClass Results:")
print(f"Total Score: {total_score:.2f}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score:.2f}")
print(f"Lowest Score: {lowest_score:.2f}")
print(f"Range of Scores: {range_of_scores:.2f}")

