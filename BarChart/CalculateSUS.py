def calculate_sus_score(responses):
    sus_score = 0

    for i in range(len(responses)):
        sus_score += responses[i] - 1
    
    sus_score *= 2.5
    return sus_score

a = [3.45, 3.64, 4.09, 3.91, 3.36, 3.18, 4.09, 4, 3.73, 3.64]
b = [2.27, 3.45, 2.09, 3.82, 3.36, 3, 2.55, 2.27, 2.73, 2.73]
c = [3.9, 4.3, 4.4, 3.8, 3.8, 4, 4.1, 4.3, 4.2, 3.7]
d = [3.4, 3.5, 3.3, 4.1, 4, 3.4, 3.2, 2.1, 2.7, 2.5]
print(calculate_sus_score(d))


# GB: 67.725 
# FB: 45.675
# GM: 76.25
# FM: 55.50