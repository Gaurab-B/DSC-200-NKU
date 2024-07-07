import pandas as pd
import requests

def first_api(): #REDDIT API(Yes authentication)
    #About the Reddit API
    #Reddit is the  Homepage of the internet
    #OAuth Authentication
    #HTTPS: YES
    #We are looking at Nepal/hot and all the data from the first page.
    client_id = "3iwTWPxViEswLNjcqb2T1Q" 
    secret_key = "9IHozPnqdNTlt4Ytwlqhe5ZOeXcj9w"
    redirect_url = 'https://www.linkedin.com/in/gaurab-baral-991333216'
    auth = requests.auth.HTTPBasicAuth(client_id,secret_key) #the auth rquest to get authorization
    #<requests.auth.HTTPBasicAuth object at 0x000001D9E034FAD0>
    data = { #my data to login
    'grant_type': 'password',
    'username': 'Beautiful-Handle-181',
    'password': 'Hahaha121212',
    'scope': 'read'
    }
    headers = {'User-Agent': 'My/Api/0.0.1'} #because reddit requires headers
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers) #getting into the system
    TOKEN = res.json()['access_token'] #get all access token from the content
    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}} #change the headers format to get access
    res = requests.get('https://oauth.reddit.com/r/Nepal/hot', headers = headers) #browse reddit.com/Nepal
    df = pd.DataFrame(columns=['subreddit', 'title', 'selftext', 'score', 'num_comments', 'author_fullname', 'link_flair_richtext'])#our essential columns
    data_list = []
    #post['data'].keys()
    for post in res.json()['data']["children"]: #for each post in the page
        data_list.append({ #get the essential data
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'score': post['data']['score'],
            'num_comments': post['data']['num_comments'],
            'author_fullname': post['data']['author_fullname'],
            'link_flair_richtext': post['data']['link_flair_richtext']
        })
    df = pd.DataFrame(data_list) #save to a csv fine
    df['author_fullname'] = df['author_fullname'].str.replace('t2_', '') #change the name by removing tw_
    print(df)
    print("\nFile saved as Group8_Lab8_firstAPI.csv")
    df.to_csv('Group8_Lab8_firstAPI.csv', index=False)

def second_api(): #Harry Potter API(No authentication)
    #Harry Potter is  a book and tv-series about fictional magical world and characters.
    #About the Harry Potter API
    #Auth: NO
    #HTTPS: YES
    #This gets the all characters and spells of harry potter.
    try:
        print("---------------------------------------------------------------------------")
        choice = int(input("Enter:\n 1: For extracting information of Harry Potter Characters. \n 2: For extracting information of Harry Potter Spells. \n 3: Go Back \n 4: End the Program\n-------------------------------------------------------------------\n"))
    except:
        print("Enter a numeric value")
    if choice == 1:
        url1 = "https://hp-api.onrender.com/api/characters"
        response = requests.get(url1) #get to the api
        data = response.json() #get the data
        df = pd.DataFrame(data) #get the data to dataframe
        df.to_csv('Group8_Lab8_HarryPotterCharacters.csv', index=False) #save to csv
        print(df)
        print("\nFile Saved as Group8_Lab8_HarryPotterCharacters.csv")
        second_api()
    elif choice == 2:
        url2 = "https://hp-api.onrender.com/api/spells"
        response2 = requests.get(url2) #get to the api
        a1 = response2.json() #get the data
        df2 = pd.DataFrame(a1) #get the data to dataframe
        df2.to_csv('Group8_Lab8_HarryPotterSpells.csv', index=False)#save to csv
        print(df2)
        print("\nFile Saved as Group8_Lab8_HarryPotterSpells.csv")
        second_api()
    elif choice == 3:
        print("Going back to the previous screen")
        return 
    elif choice == 4:
        exit(1)
    else:
        print("Invalid choice. Please enter a valid option.")

def third_api(): #DOG FACT API(No authentication)
    #About the Dog Fact API
    #Auth: No
    #HTTPS: YES
    #This is the Dog API and it provides dog facts as a service dogdog
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url) #connect to API
    data = response.json()#get data
    breeds_data = data.get('data', []) #get all data with the value Data
    final_data = [entry.get('attributes', {}) for entry in breeds_data] #get all attributes in the list for every breeds_data
    df3 = pd.DataFrame(final_data) #store in the dataframe
    columns_to_drop = ['life', 'male_weight','female_weight'] #remove these columns cause we dont need these for our purpose
    df3 = df3.drop(columns=columns_to_drop)
    print(df3)#save to a csv file
    df3.to_csv('Group8_Lab8_DogFacts.csv', index=False)
    print("\nFile Saved as Group8_Lab8_DogFacts.csv")

def fourth_api(): #CLASH OF CLANS API(Yes authentication)
    #About the Clash of Clans API
    #Clash of clans is a video game developed by supercell.
    #Auth: apiKey
    #HTTPS: YES
    #This API only runs on certain IP address. So it may not work on your device Professor.
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2NzI0ZjZkLTA5NjQtNGU3MS05ZjE0LTBkYTI1ZWQ5NThjNyIsImlhdCI6MTcwMTEwMTI3MSwic3ViIjoiZGV2ZWxvcGVyLzQ0YTJiMjU0LWRlNzQtNjBhYy0xZGY1LWU2NzYzYzM3ZGY5YiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc0LjE0My4xODAuMjQ2Il0sInR5cGUiOiJjbGllbnQifV19.ssdO6GjHt2aIitnlE9FlLZbzCE_DRHH2M2rp6EYdK_z2axEEMhF-Vdb97vpCGSher-4UVaJRRonuwA7rshvCxg',
    'Accept': 'application/json'
    }#get the aunthentication key and connect to API with the key
    response = requests.get('https://api.clashofclans.com/v1/players/%238J9P8Y0LV', headers=headers)
    user_json = response.json() #get the json format
    df = pd.json_normalize(user_json) #store all the json format to dataframe
    print(df)#save to a csv file
    df.to_csv('Group8_Lab8_ClashofClans.csv', index = False)
    print("\nFile Saved as Group8_Lab8_ClashofClans.csv")

if __name__ == "__main__": #Menu for the 4+1 API
    while True:
        print("------------------------------------------------------------------")
        print("Welcome to API Extraction System built by group 8. What would you like to do?")
        print("Enter:\n1: Get Data about r/Nepal in reddit.(Extract Reddit API)\n2: Get Data about Harry Potters.(Extract Harry Potter API)\n3: Get Data about Dogs.(Extract Dog API)\n4: Get Data about Clash of Clans(Extract Clash of Clans API)\n5: Exit")
        print("-----------------------------------------------------------------")
        try:
            choice = int(input())
        except:
            print("Please Enter a valid number")
        if choice == 1:
            first_api() #Reddit
        elif choice ==2:
            second_api() #Harry Potter
        elif choice ==3:
            third_api() #Dog Facts
        elif choice ==4:
            fourth_api()
        elif choice ==5:
            exit() #End the Program
        else:
            print(" Invalid choice. Please enter a valid option.")
        