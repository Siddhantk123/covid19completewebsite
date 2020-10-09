from django.shortcuts import render, HttpResponse, redirect
import requests
import pandas as pd
from sklearn.linear_model import LogisticRegression
from index.models import Contact
from django.contrib import messages








#reading the data
df=pd.read_csv('data.csv')
#df.head()
#df.tail()
#df.info()
#df['difficultyBreathing'].value_counts()
#df['bodyPain'].value_counts()

#test train splitting
import numpy as np

# Create your views here.
    
def index(request):

    #notification
    import requests
    from plyer import notification
    from bs4 import BeautifulSoup
    import time

    '''
    def notifyMe(title, message): #To Show The Notification
        notification.notify(
            title= title,
            message = message,
            app_icon = "virus.ico",
            timeout = 20 #Timeout Settings In Seconds
            
        )
        

    def webData(url): #Getting The Data From The Website
        r = requests.get(url)
        return r.text



    
        
    html_doc = webData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(html_doc, 'html.parser') #Parsing The Data
    mystr = ""

    for tr in soup.find_all ('tbody')[0].find_all('tr'):
        mystr += tr.get_text() #Converting the Parsed Data to a String 
                
            
            
    mystr = mystr[1:]
            
            
            
    
    myList = mystr.split("\n")
    
    
    


            
                
            

                
            



            
    states = ['Delhi','Uttar Pradesh', 'Maharashtra','Madhya Pradesh'] # Enter Your State Name Here (Dont Enter More Than 5 States)
    length=len(myList)
    
    for item in  range (length):
        #dataList = (item.split('\n'))
        #print(dataList)
        
                
        
        if myList[item] in states:
            
            
            notify_title= 'Cases of Covid-19 In India'
            notify_text= f" State: {myList[item]}\n Indian Cases : {myList[item+1]} \n Cured : {myList[item+2]}\n Deaths : {myList[item+3]}"
            notifyMe(notify_title, notify_text)
            time.sleep(5)
    #time.sleep(3600)    #Loop For 1 Hour (1 hour = 3600 seconds)         
            
'''
#    ML PART    

    def data_split(data, ratio):
        np.random.seed(42)
        shuffled= np.random.permutation(len(data))
        test_set_size= int(len(data)*ratio)
        test_indices= shuffled[ :test_set_size]
        train_indices= shuffled[test_set_size: ]
        return data.iloc[train_indices], data.iloc[test_indices]
    train, test = data_split(df, 0.2)
    #print(train)
    #print(test)

    X_train=train[['fever','bodyPain','age','runnyNose','difficultyBreathing']].to_numpy()   #converting it to an array
    #X_test=test[['fever','bodyPain','age','runnyNose','difficultyBreathing']].to_numpy()
    #print(X_train)

    Y_train=train[['infectionProb']].to_numpy().reshape(412)
    #Y_test=test[['infectionProb']].to_numpy().reshape(102)

    #print(Y_train)
    #traning
    from sklearn.linear_model import LogisticRegression
    clf=LogisticRegression()  #initialisation 
    clf.fit(X_train, Y_train)
    import math
    if request.method=="POST":
        fever=request.POST.get('fever')
        Pain=request.POST.get('Pain')
        age=request.POST.get('age')
        runnyNose=request.POST.get('runnyNose')
        diffBreath=request.POST.get('diffBreath')

        #testing
        inputFeatures= [float(fever),int(Pain),int(age),int(runnyNose),int(diffBreath)] #new data to analyse the machine
        #print(inputFeatures)
        # print(clf.predict_proba([inputFeatures]))
        # print(clf.predict([inputFeatures]))
        
        infProb= clf.predict_proba([inputFeatures])[0][1]
        e= math.ceil(infProb*100)

        exc= {'prob': e, 'var':'Your chance to be infected is= ','per':'%'}
        #print(exc)
        return render(request, 'index.html', exc)


    
    return render(request, 'index.html')



                
        


    
    



def about(request):
    return render(request,'about.htm')


def cases(request):
    def web1Data(url): #Getting The Data From The Website
        r = requests.get(url)
        return r.json() #returning it in a form of json, coz data is a json data, we can also return it in a form of text by
                        #writing r.text(), depending on the requirement
    html1_doc = web1Data('https://api.covid19india.org/raw_data16.json')





    #----now work on data by analysing the data from website----
    df=[]  #empty list
    data=html1_doc['raw_data'] #html_doc ka  raw_data store hoga data me
    for dic in data: #dic me each value aayega 
        df.append([dic['currentstatus'],dic['dateannounced'], dic['numcases'],dic['detecteddistrict'],dic['detectedstate']]) #yaha 3-3 ke pair me list me append honge  #ko fetch kr rhe #3-3 ke pair me ye list me add hoge                                                                               #ko fetch kr rhe
    #print(df)                                                                            
    #ab list mil gya us data ka and store ho ya df me





    #using the concept of data feame  of pandas
    import pandas as pd
    df=pd.DataFrame(df,columns=['CurrentStatus','Date Announced','Number of Cases','District','States'])#ye sirf heading dega frame dega
    #df me table aayega
    exc1={'table1':df.to_html()}
    #print(exc1)

            
    return render(request, 'cases.html', exc1)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            #messages.success(request, "Your message has been successfully sent
        success={'mes':'Your message has been sent !!!'}
        return render(request,'contact.html',success)    


    return render(request,'contact.html')

            




      
