header = '''<!DOCTYPE html>
<html>
<head>
    <title>[[[title]]]</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        h1 {
            color: #333;
            background-color: #f0f0f0;
            padding: 20px;
            margin: 0;
        }
        p {
            color: #666;
            padding: 20px;
            margin: 0;
        }
        @media print {
            div#issues h2 {
                page-break-before: always;
            }
        }
    </style>
</head>
<body>'''

footer = '''
    <p style="font-size: smaller;"><hr />Generert med gh2remarkable<hr /></p>
</body>
</html>'''