import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_df = df[df['education-num'] == 13]
    valid_rows = df['education-num'].dropna().shape[0]
    percentage_bachelors = round((bachelors_df.shape[0] / valid_rows) * 100, 1)  

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    advanced_and_high_salary = higher_education[higher_education['salary'] == '>50K']
    fifty_plus_percentage = round((advanced_and_high_salary.shape[0] / higher_education.shape[0]) * 100, 1)

    
    lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    lower_education_salary = lower_education[lower_education['salary'] == '>50K']
    lower_but_high_salary = round((lower_education_salary.shape[0] / lower_education.shape[0]) * 100, 1)

    
    # percentage with salary >50K
    higher_education_rich = fifty_plus_percentage
    lower_education_rich = lower_but_high_salary

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours] 
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']

    rich_percentage = round((rich_min_workers.shape[0] / min_workers.shape[0] ) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_workers = df[df['salary'] == '>50K']
    total_people_per_country = df['native-country'].value_counts()
    rich_workers_per_country = highest_earning_workers['native-country'].value_counts()
    
    
    rich_workers_per_country_percentage = (rich_workers_per_country /  total_people_per_country) * 100
    highest_earning_country_percentage = rich_workers_per_country_percentage.max().round(1)
    highest_earning_country = rich_workers_per_country_percentage.idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    highest_salary_workers = df[df['salary'] == '>50K']
    rich_indian_workers = highest_salary_workers[highest_salary_workers['native-country'] == 'India']
    rich_inidian_occupation_counts = rich_indian_workers['occupation'].value_counts()
    
    
    top_IN_occupation = rich_inidian_occupation_counts.idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
