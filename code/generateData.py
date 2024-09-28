import csv
import random
import string
import os

def generate_random_name(length=10):
    """Generate a random name with uppercase and lowercase alphabets."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def generate_csv(file_name, target_size_mb):
    """Generate a CSV file with 'name' and 'number' columns of a specified size."""
    row_size = 0
    num_rows = 0
    file_size_mb = 0
    file_path = file_name
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["name", "value"])
        
        # Keep writing rows until the file size reaches the target size in MB
        while file_size_mb < target_size_mb:
            name = generate_random_name()
            value = generate_random_number()
            writer.writerow([name, value])
            num_rows += 1
            
            # Update file size
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
            
    print(f"Generated {file_name} with {num_rows} rows and size {file_size_mb:.2f} MB")

# Generate 50 MB file
generate_csv('file_50MB.csv', 50)

# Generate 100 MB file
generate_csv('file_100MB.csv', 100)
