import requests

"""
Example to expand nested resources
(Expand 'client' field in Document Instance View)
"""

# Prepare API url to expand resource on
url = f'https://api.makeleaps.com/api/partner/{partner_mid}/document/{document_mid}/'

# Add field to expand (must be top-level) to url
expand_field = 'client'
url += f'?expand={expand_field}'

# Make a request to expansion url to expand specified field
response = requests.post(url, data=data, headers=headers)

# Retrieve expanded field
return response.json()[f'{expand_field}']
