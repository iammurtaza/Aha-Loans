import json,pandas as pd,sys,datetime,re

def main():
    args1='{"token":"AQVaPxJrvgYHltSSdeJGQl7jhU-FOf1QStpKgF0NjeWIHxHLRTKH9XHefvx3lvebHHft7RFiAQqqcuWlIpL-3_lX8Wtd-UBwPr799fcIKWUtynMmbHmWtgdQi5tFwmXu_WS5vfIkvj-TX50ZLmzp1ewn7mbJFuYPiFmM1HAgR_tHAEuZKmuM6Roi9SYZSs17YHY6STkOSSClKWb8wQ2D3mjOf45FYa273IcUentTZHKvFxVoZiATCqvdrgn2W8-B570fP4JVzMhh2qxgNSZV4UqEpzMvQdXa11nPvoz_kq0Y2xs1PaFpGxcKCn7c5OAufzYpvNe8XwHZEbOujcTqwZP3GQrQSw","refreshToken":null,"expiresIn":5183999,"id":"1iUqh2wTIA","nickname":null,"name":"Suneel Kumar Rajpoot","email":"suneelweb15@gmail.com","avatar":"https:\/\/media.licdn.com\/dms\/image\/C4D03AQHZTZnv_sKv6A\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=tUwxDAeQ0fCmFQbUgOuW7FYmNUVcROMH_280pPxWcM4","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:UUqR"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/1iUqh2wTIA"},"currentShare":{"author":{"firstName":"Suneel Kumar","id":"1iUqh2wTIA","lastName":"Rajpoot"},"comment":"","id":"s6081331427444613120","source":{"serviceProvider":{"name":"FLAGSHIP"}},"timestamp":1449902397000,"visibility":{"code":"anyone"}},"emailAddress":"suneelweb15@gmail.com","firstName":"Suneel Kumar","formattedName":"Suneel Kumar Rajpoot","headline":"SR.PHP Developer, Laravel Expert, Full Stack PHP Developer, Opencart Developer, Amazon Web Services (AWS)","id":"1iUqh2wTIA","industry":"Information Technology and Services","lastName":"Rajpoot","location":{"country":{"code":"in"},"name":"Noida Area, India"},"numConnections":500,"numConnectionsCapped":true,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C4D03AQHZTZnv_sKv6A\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=tUwxDAeQ0fCmFQbUgOuW7FYmNUVcROMH_280pPxWcM4","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C4D00AQEL0Yxaq7lGpA\/profile-originalphoto-shrink_900_1200\/0?e=1529661600&v=beta&t=iVwgnH2-8pCGMmBrsyGAllQxaRXeiGQan4ti3Z0NnBA"]},"positions":{"_total":3,"values":[{"company":{"id":15217245,"industry":"Financial Services","name":"Gullakh.com","size":"2-10","type":"Privately Held"},"id":1012766236,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"Noida Area, India"},"startDate":{"month":5,"year":2017},"title":"Senior Software Engineer"},{"company":{"id":5038819,"industry":"Retail","name":"MyFlowerTree.com","size":"51-200","type":"Privately Held"},"id":705779842,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"New Delhi Area, India"},"startDate":{"month":6,"year":2015},"title":"Senior Software Developer(PHP, Laravel, eCommerce)"},{"company":{"name":"Trust Payments Ltd"},"id":684919439,"isCurrent":true,"location":[],"startDate":{"month":6,"year":2015},"summary":"As a software Developer, I will support service specialists in performing problem determination and analysis on client systems Depending on the severity level of a problem, I will be required to work directly with clients through conference calls or on site visits and provide in sight and feedback regarding the client environment to the development organization and be responsible for existing and new product development.","title":"Senior Software Developer(laravel Framework)"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/suneelrajpoot","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAAAUvUs8Bxt2sJqHoqzokhQvfm16dmNgtSnE&authType=name&authToken=UUqR&trk=api*a5274615*s5592855*"},"summary":"Currently working as a Sr. Software Developer. My role function requires to develop code using programming specifications, high level design documents and implement the identified components based on client requirements. Its also ensure that the implemented components are unit tested and ready to beintegrated into the product. You will provide defect fixes identified by theverification team during the software development life cycle and be exposed to projects across different domains.\n\nAs a software Developer, I will support service specialists in performing problem determination and analysis on client systems Depending on the severity level of a problem, I will be required to work directly with clients through conference calls or on site visits and provide in sight and feedback regarding the client environment to the development organization and be responsible for existing and new product development.\n\nI have completed project on several platform \u2013 php, mysql, sql server 2005\/2008, oops, Joomla, Magneto, opencart, oscommerce, wordpress, DotNetNuke, virtue mart, phpfox, asp.net."},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C4D00AQEL0Yxaq7lGpA\/profile-originalphoto-shrink_900_1200\/0?e=1529661600&v=beta&t=iVwgnH2-8pCGMmBrsyGAllQxaRXeiGQan4ti3Z0NnBA"}'
    args2='{"token":"AQVv53iAgSdGNzlVuFKBYHtTiNy08Tc_zRB4se0oUqt2YNKo9dyU9arc66fGQLA6uFELZY0pfs49izRDMn_jQZLmYqRhZxUy_hXrhwlt2M-G4-ed1nt3zgrXcVwwCXh6Lv2oqeBP_EmM1vWrx0HUWnA5UW7hTW5Q5OuOr2j7wOqGtTjG88rP_gGhOZGorNfSTBM11ZX9Qdel6UP_70SIctQBWUC-E1FYqjJTKekbUkfycauvFKD4BoZ9lAn3P1zsBcN7BRBR4OnQbYjvPzTpHhObr5jw6R5NKNrp46zG-4BPZ6Em4ULA2NAjThw75jjfBrF3N4ft7tVeP_CoaSbnA5XPa5MZ0A","refreshToken":null,"expiresIn":5183999,"id":"hd-yfhQVIy","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF05Rl4FuBsyg\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=IfXypj05SD0P9_YvF5ZOHz0wmzsFt7NrpEHnNgls9lw","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:e9LX"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/hd-yfhQVIy"},"emailAddress":"sunnyyasser@gmail.com","firstName":"Sunny","formattedName":"Sunny Yasser","headline":"Data Science enthusiast","id":"hd-yfhQVIy","industry":"Computer Software","lastName":"Yasser","location":{"country":{"code":"in"},"name":"New Delhi Area, India"},"numConnections":168,"numConnectionsCapped":false,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF05Rl4FuBsyg\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=IfXypj05SD0P9_YvF5ZOHz0wmzsFt7NrpEHnNgls9lw","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C4E04AQG6jYL-4DmARg\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=DaYuHuVZSeM5P4mw5tM8jyCr8LgcpJTRPz9ja5JusY8"]},"positions":{"_total":1,"values":[{"company":{"name":"Aha! Loans , IIM Lucknow"},"id":1323599578,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"Noida Area, India"},"startDate":{"month":5,"year":2018},"summary":"Involved in the development of a credit risk analysis model using the social footprint of a person.","title":"Data Scientist Intern"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/sunny-yasser","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAACNvdAMBJFiNOLYmOX7P6a96U2pUYxO_EKc&authType=name&authToken=e9LX&trk=api*a5274615*s5592855*"},"summary":"An inquisitive, self-taught machine learning enthusiast, I look forward to collaborating in the fields of  AI and data science.\nI have experience in the development and deployment of machine learning models, including RNNs and CNNs. Proficient in Python, Pandas, Numpy, Sklearn, Keras and Tensorflow. I have experience with statistical analysis too including ROC curves, chi-squared test, and am well versed in hyperparameter tuning and exploratory data analysis.\nI also have experience in Java and C++ programming, with knowledge of data structures and algorithms. \nLooking forward to connect with opportunities in the above fields."},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C4E04AQG6jYL-4DmARg\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=DaYuHuVZSeM5P4mw5tM8jyCr8LgcpJTRPz9ja5JusY8"}'
    args3='{"token":"AQXbbk0cqH7w4MXDljwzHOwt4K5EJZfw6T3XmkZLuoeR_2qH2g7S8bsMtZcCcdllr9FWUxxLi7y0NwU7hi_o5hrvGOcVcU9r2N7X--imUVJ6GUqv2QAUtUX71DwnYxpIrHN_7oayzeNt3Y-jzidqcJkFQ14vIXn-OgHxxJ44dFWMhEh-BYq3lWE13-KAWi5I0QkmSN8Sku0HgnWk8IQlPkj73kfJAEaE68jzyKTPSBpr9TvJw6FcKotf_krXbu8CSWIq9Txf9DqDR_3X3wcRqaQCZwz_bsNyr2ywD9xPqIux6SAbRQUFSFJETvWTpAvjliETETWBZYJte6wlmj_5zhAaQ74idQ","refreshToken":null,"expiresIn":5183999,"id":"fmpR5LR-OS","nickname":null,"name":"Murtaza Hasan","email":"murtaza144482@st.jmi.ac.in","avatar":"https:\/\/media.licdn.com\/dms\/image\/C5103AQFLWA4Dy0NLSQ\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=zowTxq1FAlY_8ekEAk6-lXwPPoSmHGKfYRUFhmEf8XE","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:wKXO"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/fmpR5LR-OS"},"currentShare":{"author":{"firstName":"Murtaza","id":"fmpR5LR-OS","lastName":"Hasan"},"comment":"Curiously enough a course on learning is the highest rated MOOC on the internet. I wondered why would anyone need to learn how to learn and then I did this course and got my answer.\n\nThis is an amazing course which I would recommend to anyone ranging from a 6th grader right to someone doing a PhD.\u00a0It will forever change your perspective on learning new skills.\n\nI am thankful to Dr Barbara Oakley and Dr Terrence Sejnowski for their extensive research and methodology of teaching. The write-ups following the videos, recommended articles, creative assignments, optional interviews, a community of learners helping each other\u00a0and learners making rap videos, animations, poems about what they were taught, everything was spot on.\n\nThis course really signified to me what effective learning could be and should be.\u00a0\n\nGraded Certification Link:\u00a0https:\/\/lnkd.in\/f8-aJAC","id":"s6399948055751294976","source":{"serviceProvider":{"name":"LINKEDIN"}},"timestamp":1525866521777,"visibility":{"code":"anyone"}},"emailAddress":"murtaza144482@st.jmi.ac.in","firstName":"Murtaza","formattedName":"Murtaza Hasan","headline":"Data Science Intern at Aha! Loans","id":"fmpR5LR-OS","industry":"Computer Software","lastName":"Hasan","location":{"country":{"code":"in"},"name":"New Delhi Area, India"},"numConnections":500,"numConnectionsCapped":true,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C5103AQFLWA4Dy0NLSQ\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=zowTxq1FAlY_8ekEAk6-lXwPPoSmHGKfYRUFhmEf8XE","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C5100AQHLJA2bizGynA\/profile-originalphoto-shrink_450_600\/0?e=1529668800&v=beta&t=74DuRouIfb4KCTjL-gD9FihDRaYGxyD_SoOZPU5vduw"]},"positions":{"_total":1,"values":[{"company":{"name":"Aha! Loans"},"id":1321666935,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"Noida Area, India"},"startDate":{"month":5,"year":2018},"title":"Data Science Intern"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/murtaza-hasan","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAABxIydIBsuGcovfpDqmnwlwtGmhKJ7GEO5w&authType=name&authToken=wKXO&trk=api*a5274615*s5592855*"},"summary":"I believe intelligence is dynamic and all skills can be acquired with practice and determination"},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C5100AQHLJA2bizGynA\/profile-originalphoto-shrink_450_600\/0?e=1529668800&v=beta&t=74DuRouIfb4KCTjL-gD9FihDRaYGxyD_SoOZPU5vduw"}'
    args4='{"token":"AQX9Sp9OsSsPE0d1_6sSQNcwjDoeayRwQjXqiNJMc_lyoB2wxfDXrAYSkNkzBUZ1kzcjdbBt13Xr0WsW2pTmUHnhGJZX9w_Jm1bpoKuEgoUhFI0mHH4dKsnG6BJT-ApwEiz9IwNAWDuGLm5mA3X7kJvz65GV9c4ddkFk9ADIl7h2bkp8ip9zs-jMWL6Q70LcQg_oPHTOpXAkXlU3HF6KuUvrsSGWMcdlfKJ6EXIin2_1Dv0gf6JpNsrjEn81mYs5V0OcIL4ljB9pBn7EyV5ts0fTsJ5P7SJrp93pwHGt7K0HtWXf3-jvRr0b5kCxfhUHMwyfxrbW5RLcjD3DVfbVq_7B6iY9EA","refreshToken":null,"expiresIn":5183999,"id":"ynWKHJCIzs","nickname":null,"name":"Akbar Ali","email":"akbarrizvi2000@yahoo.co.in","avatar":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF7gFhuhlvaRQ\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=7bWZNcEAL6V8OGzoSjSjS8zXvAfvn98evqLQkG6-jiY","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:9a17"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/ynWKHJCIzs"},"currentShare":{"author":{"firstName":"Akbar","id":"ynWKHJCIzs","lastName":"Ali"},"comment":"Know your credit card","id":"s6274972422978572288","source":{"serviceProvider":{"name":"FLAGSHIP"}},"timestamp":1496070008000,"visibility":{"code":"connections-only"}},"emailAddress":"akbarrizvi2000@yahoo.co.in","firstName":"Akbar","formattedName":"Akbar Ali","headline":"Co-founder at gullakh.com","id":"ynWKHJCIzs","industry":"Banking","lastName":"Ali","location":{"country":{"code":"in"},"name":"New Delhi Area, India"},"numConnections":500,"numConnectionsCapped":true,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF7gFhuhlvaRQ\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=7bWZNcEAL6V8OGzoSjSjS8zXvAfvn98evqLQkG6-jiY","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C5104AQFLedqaIxjwMQ\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=8Z6tlC0C5kBGiKowha6jPLv0Y2wADJQkzN4q9cRQMhk"]},"positions":{"_total":1,"values":[{"company":{"id":15217245,"industry":"Financial Services","name":"Gullakh.com","size":"2-10","type":"Privately Held"},"id":853829217,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"New Delhi Area, India"},"startDate":{"month":5,"year":2016},"title":"Co-founder at gullakh.com"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/akbar-ali-co-founder-gullakh","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAAAYkjz4BAenvM7kWSoEdDcD07uq_uJjmfI8&authType=name&authToken=9a17&trk=api*a5274615*s5592855*"},"summary":"I am an MBA from University of Lucknow and a Certified Associate of Indian Institute of Bankers from IIBF, Mumbai with over 12 years of Retail Banking work experience in both retail assets and liabilities group.\nIn 2016, launched a financial marketplace called www.gullakh.com with a few old friends to change the way people shop for retail loan. "},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C5104AQFLedqaIxjwMQ\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=8Z6tlC0C5kBGiKowha6jPLv0Y2wADJQkzN4q9cRQMhk"}'

    #args4=args4.replace('null','\"null\"') 
    value=json.loads(args4,strict=False)

    print("LINKEDIN SCORE\n")
    print(linkedinScore(value))
   

def linkedinScore(value):
    total_score=0

    industryScore=pd.read_csv('industryscore.csv')
    companyList=pd.read_csv('comapnyList.csv')
    locationList=pd.read_csv('locationList.csv')

    locationList.set_index("Branch Name",inplace=True)
    companyList.set_index("CATEGORY",inplace=True)

    if(value['user']['location'] and value['user']['location']['name']):
        area=value['user']['location']['name'].split(',')[0].split(' ')[:-1]
        ccode=value['user']['location']['country']['code']
        location=" ".join(area).strip()
        try:
            idx=locationList.loc[locationList['City'].values == location]['Location type PL'][0]
            #print(total_score)
            if(idx=='Type A PL'):total_score+=100
            elif(idx=='Type B PL'):total_score+=50
            else:pass
        except:
            pass

    if(value['user']['positions'] and value['user']['positions']['_total'] is not 0 ):
        pos=value['user']['positions']['values']
        start_month=0
        start_year=0
        company_name=0
        for item in pos:
            if(item['company']):
                company_name=item['company']['name']
            elif(item['startDate']):
                start_month=item['startDate']['month']
                start_year=item['startDate']['year']
            else:pass

    try:
        now=datetime.datetime.now()
        years_passed=now.year-int(start_year)
        if(years_passed==0):pass
        elif(years_passed <=1):total_score+=10
        elif(years_passed>1 and years_passed<=2):total_score+=20
        elif(years_passed>2 and years_passed<=3):total_score+=30
        elif(years_passed>3 and years_passed<=5):total_score+=40

        else:total_score+=50

    except:
        pass

    try:
        idx=companyList.index[companyList['COMPANY NAME'].values == company_name][0]
        if(idx == 'A+'):total_score+=100
        elif(idx == 'C1000'):total_score+=80
        elif(idx == 'Cat A'):total_score+=60
        elif(idx == 'Cat B'):total_score+=40
        elif(idx == 'Cat G'):total_score+=20
        else:pass
        
    except:
        pass

    if(value['user']['industry']):
        industry=value['user']['industry']
        try:
            idx=industryScore.index[industryScore['Industry']== industry][0]
            total_score+=idx
            
        except:pass
    else:pass    

    if (value['user']['headline']):
        
        try:
            headline=value['user']['headline'].lower()
            looking='looking'
            _for='for'
            job='job'
            contains_1=re.compile(looking.lower())
            contains_2=re.compile(_for.lower())
            contains_3=re.compile(job.lower())
            if(contains_1.search(headline) and contains_2.search(headline) and contains_3.search(headline) ):pass
            elif(contains_1.search(headline) and contains_3.search(headline)):pass
            elif(contains_1.search(headline) and contains_2.search(headline)):total_score+=30
            else:total_score+=50    
            
        except: 
            pass

    if(value['user']['numConnections']):
        if(value['user']['numConnectionsCapped']):
            total_score+=50
        else:
            total_score+=int (int(value['user']['numConnections'])/10)    

    if(value['name'] and value['email']):
        try:
            first_name=value['name'].split()[0]
            last_name=value['name'].split()[1]
            email=value['email']
            contains_f=re.compile(first_name.lower())
            contains_l=re.compile(last_name.lower())
            if(contains_f.search(email.lower()) and contains_l.search(email.lower()) ):total_score+=25
            elif(contains_f.search(email.lower()) or contains_l.search(email.lower())):total_score+=25
            else:pass    
        except:pass

    return(int(total_score))

if __name__ == '__main__':
    main()
