with open ('data.txt', 'r') as file:
    lines = file.readlines()

with open('filtered_data.txt', 'w') as filtered_data:
    for line in lines:
        if line.strip():
            filtered_data.write(line)

