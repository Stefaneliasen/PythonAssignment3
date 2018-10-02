from webget import download
from deaths_lib import countDeaths, countList
# Download file for usage
download("https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD", name='deaths.txt')

with open('./download/deaths.txt', 'r') as fp:
    content = fp.read()
    
def main():
    pass

if __name__ == '__main__':
    main()
#Split lines
lineArray = content.splitlines()

# 1. Which state has the most deaths in the year of 2016? (All causes)

most_deaths = countDeaths(lineArray, "2016", "All Causes")
print(most_deaths)

# 2. Which state has the least deaths in the year of 2016? (All causes)

least_deaths = countDeaths(lineArray, "2016", "All Causes", "Lowest")
print(least_deaths)

# 3. Which state has had the smallest increase in deaths from 1999-2016? (All causes)

states1999 = countDeaths(lineArray, "1999", "All Causes", "All")

states2016 = countDeaths(lineArray, "2016", "All Causes", "All")

countList(states1999, states2016)

# 4. Which state has the most deaths caused by kidney disease in the year of 2005?

KD_most_deaths = countDeaths(lineArray, "2005", "Kidney disease")
print(KD_most_deaths)

# 5. Which state has had the biggest increase in the death of Alzheimers from 1999-2016? Plot the increase year for year using matplotlib

