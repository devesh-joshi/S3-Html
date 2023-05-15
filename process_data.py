# Read the data from the file
try:
    with open("app_final_result.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("Error: File not found.")
    exit(1)


# Prepare the HTML content
html = """
<html>
<head>
    <title>Result</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Application</th>
            <th>Region</th>
            <th>Version</th>
            <th>Result</th>
        </tr>
"""

# Parse the data and generate table rows
for line in data:
    values = line.strip().split("|")
    html += f"""
        <tr>
            <td>{values[0]}</td>
            <td>{values[1]}</td>
            <td>{values[2]}</td>
            <td>{values[3]}</td>
        </tr>
    """

# Complete the HTML content
html += """
    </table>
</body>
</html>
"""

# Write the HTML content to a file
with open("result.html", "w") as file:
    file.write(html)
