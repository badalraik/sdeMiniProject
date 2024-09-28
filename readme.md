Performance Comparison of Data Processing: Cloud vs. Local Setup

==========================  Project Overview    ==========================

This project demonstrates the performance difference between processing large datasets in a local environment and on Google Cloud. We use Python scripts to process CSV files, generate performance metrics, and create comparative bar graphs.

==========================  File Structure  ==========================

barGraph/: Contains the generated bar graphs comparing cloud and local setups.
code/: Contains the Python scripts for data generation, processing, and graph creation.
data/: Generated data files (50MB and 100MB CSV files).
runReport/: The folder where performance reports are saved.

==========================  Requirements    ==========================

Python 3.x

Libraries:

pandas
matplotlib
timeit
numpy

Google Cloud SDK (for cloud-based processing)

==========================  Steps to Run Locally    ==========================

1. Clone the repository:

git clone https://github.com/your-repo-link.git
cd your-repo-link

2. Generate Data:

python code/generate_data.py

3. Process Data Locally:

python code/process_data.py --local

4. Process Data on Google Cloud:

Upload data to Google Cloud Storage and run process_data.py on Cloud Shell.

5. Generate Metrices

/usr/bin/time -v python3 processData.py

6. Generate Performance Comparison Graph:

python code/generate_bar_graph.py

==========================  Performance Comparison  ==========================

The project compares the execution time and resource usage between cloud-based and local setups. A bar graph visualizing the differences is stored in the barGraph/ directory.