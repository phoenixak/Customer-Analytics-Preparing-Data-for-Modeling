import pandas as pd

# Load the dataset
ds_jobs = pd.read_csv("dataset\customer_train.csv")

# Copy the DataFrame for cleaning
ds_jobs_clean = ds_jobs.copy()

# Create a dictionary of columns containing ordered categorical data
ordered_cats = {
    'relevant_experience': ['No relevant experience', 'Has relevant experience'],
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

# Loop through DataFrame columns to efficiently change data types
for col in ds_jobs_clean:
    
    # Convert integer columns to int32
    if ds_jobs_clean[col].dtype == 'int':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('int32')
    
    # Convert float columns to float16
    elif ds_jobs_clean[col].dtype == 'float':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('float16')
    
    # Convert columns containing ordered categorical data to ordered categories using dict
    elif col in ordered_cats.keys():
        category = pd.CategoricalDtype(ordered_cats[col], ordered=True)
        ds_jobs_clean[col] = ds_jobs_clean[col].astype(category)
    
    # Convert remaining columns to standard categories
    else:
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('category')
        
# Filter students with 10 or more years experience at companies with at least 1000 employees
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]