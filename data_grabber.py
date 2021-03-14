import requests 
import time

# Call the endpoint to get the data string from the sensor every 30 min for 24 $
for i in range(48):
     # Get call back
     data_file = open('data.txt', 'a')
     response = requests.get("http://192.168.30.146/")
     data_file.write(response.content.decode('utf-8') + "\n")
     data_file.close()
     print("Line: {0} completed -> {1}".format(i, response.content.decode('utf-$')))
     time.sleep(60*30)
