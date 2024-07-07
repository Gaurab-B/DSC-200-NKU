#Group 8: Gaurab Baral and Aaditya Khanal ; Lab 7
#Python 3.11.4 64-bit
#import the essential libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
#task 2 does web scraping of google finance
def task2(url1):
    value = requests.get(url1)
    soup = BeautifulSoup(value.content, 'html.parser')
    content = soup.find_all("div", class_ = "e1AOyf")
    outer_list = []
    for item in content:
        each_box = item.find_all("div", class_="PieIgb") #outer box
        for name in each_box:   

            company_name = name.find("div", class_="RwFyvf").get_text() #name of the company
            current_value = name.find("div", class_="YMlKec").get_text() #stock value
            change_element = name.find("div", class_="JwB6zf").get_text() #find the change in price of stick
            change_text = name.find("span" , class_ = ["NydbP nZQ6l","NydbP VOXKNe"])#change can be + or -
            aria_label = change_text["aria-label"] #check aria level attribute for up or down change
        # Determine if "Up" or "Down" is in the change text
            if "Down" in aria_label:
                change_element = "-" + change_element  # Make it negative
            outer_list.append([company_name, current_value, change_element])
    df = pd.DataFrame(outer_list, columns = ["Company Name","Stock Price($)","Change in percentage"])
    df["Change in percentage"] = df["Change in percentage"].str.rstrip('%').astype(float) #toremove % from the columns)
    df["Stock Price($)"] = df["Stock Price($)"].str.replace('[$,]', '', regex=True).astype(float) #remove $ from the stock price
    df["Company Name"] = df["Company Name"].str.replace(',', '') #remove comma from the name for csv file 
    df.to_csv("group_8_task2.csv", index = False) #save to a csv file
    print("---------------------------------------------------------")
    print("File saved as group_8_task2.csv")
    print("Number of rows:", len(df))#display rows and columns
    print("Number of columns:", len(df.columns))
    print("Task 2 Complete")
    print("---------------------------------------------------------")

#this web scrapes vincentarelbundock.github.
def task3part1(url2):
    labt3a = requests.get(url2)
    soup = BeautifulSoup(labt3a.text, 'html.parser')
    tr_elements = soup.find_all('tr')#get all tr
    href_list = []
    for tr_element in tr_elements:
        for td in tr_element.find_all('td'): #get all td
            if td.text.strip() == "CSV": #find the td with CSV in its text part
                a_element = td.find('a') #get the anchor element
                href = a_element.get('href') #get the link to the csv file
                href_list.append(href) #store all the links in a list
    random_csv_url = random.choice(href_list) #get a random link from the list
    response = requests.get(random_csv_url) #open the link
    with open("group_8_task3part1_vincentarelbundock_github.csv", 'wb') as csv_file:
        csv_file.write(response.content) #save to a csv file
    df = pd.read_csv("group_8_task3part1_vincentarelbundock_github.csv")
    print("---------------------------------------------------------")
    print("The downloaded file is:", random_csv_url )
    print("Number of rows:", len(df))#display rows and columns
    print("Number of columns:", len(df.columns))
    print("Task 3 part 1 Complete")
    print("---------------------------------------------------------")


def task3part11(url2): #this is to extract the webpage that had CSV files
    labt3a = requests.get(url2)
    soup = BeautifulSoup(labt3a.text, 'html.parser')
    dataframe_table = soup.find('table', class_='dataframe')
    headers = [th.text.strip() for th in dataframe_table.find_all('th')] #all header values from the table
    data = []
    for row in dataframe_table.find('tbody').find_all('tr'): #get all tr
            columns = [td.text.strip() for td in row.find_all('td')] #get all td
            data.append(columns)
    df = pd.DataFrame(data, columns=headers) #make dataframe
    df = df.loc[1:] #remove the NONE line
    # Saving the DataFrame to a CSV file
    df.to_csv('group8_contents.csv', index=False,header=headers, encoding='utf-8')
    print("---------------------------------------------------------")
    print("The csv file content saved  is: group8_contents.csv")
    print("Number of rows:", len(df))#display rows and columns
    print("Number of columns:", len(df.columns))
    print("---------------------------------------------------------")

#this webscrapes realpython.github.io/fake-jobs
def task3part2(url3):
    page = requests.get(url3)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all("div", class_ = "card-content")
    outer_list = [["job_title", "company_name", "city", "state", "posting_date"]]
    for element in content:
        list = []
        # Find and extract the title
        title = element.find('h2').text.strip()
        
        # Find and extract the company
        company = element.find('h3').text.strip() 
        
        # Find and extract the location
        location = element.find('p', class_="location").text.strip()
        result = location.split(',')
        # Find and extract the time
        time = element.find('time').text.strip()
        list = [title,company,result[0],result[1],time]
        outer_list.append(list)
    data = outer_list[1:] #start from 1 as index 0 is the title
    df = pd.DataFrame(data, columns=outer_list[0])
    df.to_csv("group_8_task3part2_realpython_github_io_fake-jobs.csv", index = False)#save to a csv file
    print("---------------------------------------------------------")
    print("File saved as group_8_task3part2_realpython_github_io_fake-jobs.csv")
    print("Number of rows:", len(df)) #display rows and columns
    print("Number of columns:", len(df.columns))
    print("Task 3 part 2 Complete")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Please enter the number:\n1: Solve Task 2 (Scrape Google Finance)\n2: Solve Task 3 Part 1 (Scrape vincentarelbundock.github.io)\n3: Solve Task 3 Part 2 (Scrape realpython.github.io/fake-jobs)\n4: Exit\n"))
            if choice == 1:
                url1 = "https://www.google.com/finance/?hl=en"
                task2(url1)
            elif choice == 2:
                url2 = "https://vincentarelbundock.github.io/Rdatasets/datasets.html"
                task3part11(url2)
                task3part1(url2)
            elif choice == 3:
                url3 = "https://realpython.github.io/fake-jobs/"
                task3part2(url3)
            elif choice == 4:
                break  # Exit the loop if the user chooses to exit
            else:
                print("Please enter a valid choice (1, 2, 3, or 4).")
        except ValueError:
            print("Please enter an integer value.")