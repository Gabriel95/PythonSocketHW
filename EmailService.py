import requests
import DataEngine
def send_simple_message(username):
    user = DataEngine.searchFromFile(username)
    elements = user.split(', ')
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd3d6bb74e0ca4dbf9e7fff35e6b86833.mailgun.org/messages",
        auth=("api", "key-0837599a748e1ed8c4b9c5f0662d7a11"),
        data={"from": "noreply@pythonsocket.com",
              "to": elements[2],
              "subject": "Client Info",
              "text": "Here is your Contact Info:",
              "html": """
                    <html>
                    <h5>Username: """ + elements[0] + """</h5>
                    <h5>Name: """ + elements[1] + """</h5>
                    <h5>Email: """ + elements[2] + """</h5>
                     <h5>Id: """ + elements[3] + """</h5>
                    <h5>Birthday: """ + elements[4] + """</h5>
                    <img src=""" + elements[5] + """>
                    <html>
              """})