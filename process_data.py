import csv
import json

# Read the JSON data from the file
with open('result.txt', 'r') as file:
    data = json.load(file)

# Generate the CSV content
csv_content = []
for item in data:
    csv_content.append([item['Application'], item['Region'], item['Version'], item['result']])

# Write the CSV content to a file
with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(csv_content)

# Generate the HTML content
html = '''
<html>
<head>
    <title>Result</title>
</head>
<body>
    <table>
        <tr>
            <th>Application</th>
            <th>Region</th>
            <th>Version</th>
            <th>Result</th>
        </tr>
'''

for row in csv_content:
    html += f'''
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>
    '''

html += '''
    </table>
</body>
</html>
'''

# Write the HTML content to a file
with open('result.html', 'w') as file:
    file.write(html)
