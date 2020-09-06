import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # User needs to make sure that enters the city's name correctly (It is not case sensitive). If the name is not entered correctly, the       user is prompted to enter it again.
    cities = ['chicago','new york city','washington']

    while True:
        try:
            city = str(input('Would you like to analyze the data for Chicago, New York City or Washington?\n')).lower()
            if city in cities:
                print('\nLet\'s review the information for {}!'.format(city.title()))
                break
            else:
                print('\nThat\'s not a valid city! Make sure you enter Chicago, New York City or Washington.')
        except:
            print('\nThat\'s not a valid city! Make sure you enter Chicago, New York City or Washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    # User needs to make sure that enters the month's name correctly (It is not case sensitive). If the name is not entered correctly, the       user is prompted to enter it again.
    #If the user doesn't want to apply a filter, a 'None' is required.
    months = ['january','february','march','april','may','june']

    while True:
       try:
           month = str(input('\nWould you like to analyze the data for January, February, March, April, May or June? If you won\'t like to apply a month filter, type the option \'None\'.\n')).lower()
           if month in months:
               print('\nLet\'s review the information for {}!'.format(month.title()))
               break
           elif month == 'none':
               print('\nLet\'s review the information for all months!')
               break
           else:
               print('\nThat\'s not a valid month! Make sure you enter January, February, March, April, May, June or None for no filter.')
       except:
           print('\nThat\'s not a valid month! Make sure you enter January, February, March, April, May, June or None for no filter.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # User needs to make sure that enters the day's name correctly (It is not case sensitive). If the name is not entered correctly, the         user is prompted to enter it again.
    #If the user doesn't want to apply a filter, a 'None' is required.
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    while True:
       try:
           day = str(input('\nWould you like to analyze the data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? If you won\'t like to apply a day filter, type the option \'None\'.\n')).lower()
           if day in days:
               print('\nLet\'s review the information for {}!'.format(day.title()))
               break
           elif day == 'none':
               print('\nLet\'s review the information for all the days of the week!')
               break
           else:
               print('\nThat\'s not a valid day! Make sure you enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or None for no filter.')
       except:
           print('\nThat\'s not a valid month! Make sure you enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or None for no filter.')


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) most_common_month: name of the most common or the selected month
        (str) most_common_day: name of the most common or the selected day of week
        (str) most_common_hour: name of the most common start hour

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common or the selected month
    months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}

    most_common_month = df['month'].mode()[0]
    print('Selected month/most common month: {}'.format(months[most_common_month]))

    # display the most common or the selected day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Selected day/most common day: {}'.format(most_common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common hour: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

     Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) most_common_start_station: name of the most popular start station
        (str) most_common_end_station: name of the most popular end station
        (str) most_common_combination: name of the most popular combination (start station - end station)

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most popular Start Station: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most popular End Station: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most popular combination (Start Station - End Station): {}'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (float) total_travel_time: total travel time in seconds for the trips within the filter
        (float) avg_travel_time: avergae travel time in seconds for the trips within the filter

    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time (secs): {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Mean travel time (secs): {}'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

     Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (int) user_types: counts per user type within the filter
        (int) gender_counts: counts per gender within the filter
        (int) min_birth: earliest birth year of the users within the filter
        (int) max_birth: moest recent birth year of the users within the filter
        (int) most_common_birth: most common birth year of the users within the filter
        (int) raw_data: number of rows displayed for raw datayes

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    while True:
        try:
            # TO DO: Display counts of gender
            gender_counts = df['Gender'].value_counts()
            print('\n')
            print(gender_counts)

            # TO DO: Display earliest, most recent, and most common year of birth
            min_birth = int(df['Birth Year'].min())
            print('\nEarliest birth year: {}'.format(min_birth))

            max_birth = int(df['Birth Year'].max())
            print('Most recent birth year: {}'.format(max_birth))

            most_common_birth = int(df['Birth Year'].mode()[0])
            print('Most common birth year: {}'.format(most_common_birth))
            break

        except:
            print('\nFor Washington there\'s unfortunately no information about users\' gender and birth year.')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print(df.head())
    raw_data = 5

    while True:
        try:
            more_data = str(input('Would you like to see more data? Enter yes or no.\n')).lower()
            if more_data == 'no':
                print('\nYou\'ve selected not to retrieve more data, thank you for your confirmation.')
                break
            elif more_data =='yes':
                raw_data = raw_data + 5
                print(df.head(raw_data))
                print('\nYou\'ve selected the option to retrieve data for {} rows.'.format(raw_data))
            else:
                print('\nThat\'s not a valid answer! Make sure you enter \'yes\' or \'no\'.')

        except:
            print('\nThat\'s not a valid answer! Make sure you enter \'yes\' or \'no\'.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
