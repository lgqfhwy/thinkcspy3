
# # Sending Email
# import smtplib, email.mime.text

# me = "lgq0915@163.com"       # Put your own email here
# fred = "909848102@qq.com"   # And fred's email address here
# your_mail_server = "mail.my.org.com"    # Ask your system administrator

# # Create a text message containing the body of the email
# # You should read this from a file, of course.
# msg = email.mime.text.MIMEText(""" Hey Fred,

# I'm having a party, please come at 8pm.
# Bring a plate of snacks and your own drinks.

# Joe""")

# msg["From"] = me   # Add headers to the message object
# msg["To"] = fred
# msg["Subject"] = "Party on Saturday 23rd"

# # Create a connection to your mail server
# svr = smtplib.SMTP(your_mail_server, 25)
# response = svr.sendmail(me, fred, msg.as_string())  # Send message
# if response != {}:
#     print("Sending failed for ", response)
# else:
#     print("Message sent.")

# svr.quit()

# Write your own web server
# from codecs import latin_1_encode
# from wsgiref.simple_server import make_server

# def my_handler(environ, start_response):
#     path_info = environ.get("PATH_INFO", None)
#     query_string = environ.get("QUERY_STRING", None)
#     response_body = "You asked for {0} with query {1}".format(
#                         path_info, query_string)
#     response_headers = [("Content-Type", "text/plain"),
#             ("Content-Length", str(len(response_body)))]
#     start_response("200 OK", response_headers)
#     response = latin_1_encode(response_body)[0]
#     return [response]

# httpd = make_server("127.0.0.1", 8000, my_handler)
# httpd.serve_forever()   # Start the server listening for requests


from codecs import latin_1_encode
from wsgiref.simple_server import make_server
import time
def my_handler(environ, start_response):
    path_info = environ.get("PATH_INFO", None)
    if path_info == "/gettime":
        response_body = gettime(environ, start_response)
    elif path_info == "/classlist":
        response_body = classlist(environ, start_response)
    else:
        response_body = ""
        start_response("404 Not Found", [("Content-Type", "text/plain")])
    response = latin_1_encode(response_body)[0]
    return [response]

def gettime(env, resp):
    html_template = """ <html>
    <body bgcolor = 'lightblue'>
     <h2>The time on the server is {0}</h2>
    <body>
    </html>
    """
    response_body = html_template.format(time.ctime())
    response_headers = [("Content-Type", "text/html"),
            ("Content-Length", str(len(response_body)))]
    resp("200 OK", response_headers)
    return response_body

def classlist(env, resp):
    return      # Will be written in the next section!

httpd = make_server("127.0.0.1", 8000, my_handler)
httpd.serve_forever()   # Start the server listening for requests












