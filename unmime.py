import quopri

with open('test.html', 'r') as f:
    encoded_content = f.read()

decoded_content = quopri.decodestring(encoded_content).decode('utf-8')
print(decoded_content)
