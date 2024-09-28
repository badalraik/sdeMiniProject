import pandas as pd
import timeit

# Path to local CSV file
file_path = 'large_dataset.csv'
# file_path = 'file_50MB.csv'
# file_path = 'file_100MB.csv'    

def process_data():
    # Read CSV file
    data = pd.read_csv(file_path)

    # Example data processing: Filter rows where 'value' column > 100
    filtered_data = data[data['value'] > 10]
    
    # Calculate aggregate: Sum of 'value' column
    total_value = filtered_data['value'].sum()

    print(f"Total value after filtering: {total_value}")
    return total_value

if __name__ == '__main__':
    # Measure the execution time
    execution_time = timeit.timeit('process_data()', globals=globals(), number=1)
    print(f"Execution time: {execution_time:.2f} seconds")
