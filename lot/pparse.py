from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
# initialize an HTTP session
session = HTMLSession()

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details 

def out(car_reg_no):
        url = "http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx"
        # get all form tags
        forms = get_all_forms(url)
        # iteratte over forms
        for i, form in enumerate(forms, start=1):
            form_details = get_form_details(form)
            print("="*50, f"form #{i}", "="*50)
            # print(form_details)  


        first_form = get_all_forms(url)[0]
        form_details = get_form_details(first_form)

        data = {}
        for input_tag in form_details["inputs"]:
            if input_tag["type"] == "hidden":
                # if it's hidden, use the default value
                data[input_tag["name"]] = input_tag["value"]
            elif input_tag["name"] == 'ctl00$ContentPlaceHolder1$txtRegNo':
                data[input_tag["name"]] = car_reg_no        
            elif input_tag["type"] != "submit":
                # all others except submit, prompt the user to set it
                # value = input(f"Enter the value of the field '{input_tag['name']}' (type: {input_tag['type']}): ")
                data[input_tag["name"]] = ''
        data["ctl00$ScriptManager1"] = "ctl00$ContentPlaceHolder1$updatePanel|ctl00$ContentPlaceHolder1$btnShow"
        data["ctl00$ContentPlaceHolder1$RadioButtonList1"] = "EXT"
        data["ctl00$ContentPlaceHolder1$ddlNavigationPage"] = "GenericDetails"
        del data["btnCancel"]
        data["ctl00$ContentPlaceHolder1$btnShow"] = "Submit"
        data["__ASYNCPOST"] = "false"
        url = urljoin(url, form_details["action"])

        if form_details["method"] == "post":
            res = session.post(url, data=data)
        elif form_details["method"] == "get":
            res = session.get(url, params=data) 
        soup = BeautifulSoup(res.content, "html.parser")
        a = soup.find('tr', class_='GridItem')
        b = a.find_all('td')
        print(len(b))
        numb = b[2].get_text()
        owner = b[5].get_text()
        car_manu = b[13].get_text()
        model = b[14].get_text()
        typee = b[12].get_text()
        print("hello {} owner of beautiful {} {} with registration number {} which is {}".format(owner,car_manu,model,numb,typee))  
        return{'reg_no':numb,'owner':owner,'manu':car_manu,'model':model,'typee':typee}  
        print("hello {} owner of beautiful {} {} with registration number {} which is {}".format(owner,car_manu,model,numb,typee))  
      

# for i in soup.find_all("tbody"):
#     print(i)

# for link in soup.find_all("link"):
#     try:
#         link.attrs["href"] = urljoin(url, link.attrs["href"])
#     except:
#         pass
# for script in soup.find_all("script"):
#     try:
#         script.attrs["src"] = urljoin(url, script.attrs["src"])
#     except:
#         pass
# for img in soup.find_all("img"):
#     try:
#         img.attrs["src"] = urljoin(url, img.attrs["src"])
#     except:
#         pass
# for a in soup.find_all("a"):
#     try:
#         a.attrs["href"] = urljoin(url, a.attrs["href"])
#     except:
#         pass

# # write the page content to a file
# # open("page.html", "w").write(str(soup))
# with open("page.html", "w", encoding="utf-8") as f:
#     f.write(str(soup))

# import webbrowser
# # open the page on the default browser
# webbrowser.open("page.html")