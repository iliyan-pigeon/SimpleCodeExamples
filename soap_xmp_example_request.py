from suds.client import Client

# URL to the WSDL file
wsdl = 'http://www.example.com/service?wsdl'

# Create a client
client = Client(wsdl)

# Call a service method
response = client.service.method_name(param1="value1", param2="value2")

print(response)
