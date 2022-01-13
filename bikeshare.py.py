import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Specify a city, month, and day to analyze bikeshare data.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter chicago, new york city, or washington: ").lower()

        if city in ['chicago', 'new york city', 'washington']:
            print('correct input!')
            break
        else:
            print('Oops!, invalid city, kindly enter chicago, new york city or washington.')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month within the first six months or enter "all": ').lower()

        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('correct input!')
            break
        else:
            print('invalid month, please check for spelling errors and try again.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter any day of the week e.g Sunday or enter "all": ').lower()

        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('correct input!')

            print('\nCalculating Statistics................')
            break
        else:
            print('invalid day, please check for spelling errors and try again.')


    print('-'*100)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    print('Most common month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of week:', common_day_of_week)

    # To display the most common start hour

    # first we extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Now we display the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]

    print('most commonly used start station:', most_used_start_station)

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]

    print('most commonly used end station:', most_used_end_station)


    # display most frequent combination of start station and end station trip
    most_used_start_and_end_station = (df['Start Station'] + df['End Station']).mode()[0]

    print('most commonly used  start station and end station:', most_used_start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time:',total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser Statistics...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_usertypes = df['User Type'].value_counts()

    print('counts of user types:',counts_of_usertypes)


    # Display counts of gender
    if "Gender" in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of genders:',counts_of_gender)

    else: print('Gender not found')


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_date_of_birth = df['Birth Year'].min()
        latest_date_of_birth = df['Birth Year'].max()
        most_common_date_of_birth = df['Birth Year'].mode()[0]

        print('earliest year of birth:',      earliest_date_of_birth)
        print('most recent year of birth:',   latest_date_of_birth)
        print('most common year of birth:',   most_common_date_of_birth)

    else:print('Birth Year does not exist"')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


    # iterating through the raw data in chucnks of 5 observations per iteration
    start_loc = 0
    end_loc= 5
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data =="yes":
            print(df.iloc[start_loc:end_loc])
            df.reset_index()
            start_loc += 5
            end_loc += 5
            view_data = input("Do you wish to continue?: Enter yes or no.\n").lower()
        if view_data == 'no':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
