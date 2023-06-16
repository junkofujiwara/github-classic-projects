## GitHub repository project (classic) maintenance script

### Prerequisites
Python 3
`pip install -r requirements.txt`

### Usage: List classic repository projects
Purpose: projects information within a specified organization/repository.<br/>
How to Use: Execute following command-line with your organization name, repository name, and token (Personal Access Token). The list of repository projects (classic) information is written to a csv file `projects.csv`.

- Command-line: 
`python3 projects.py list -o <org-name> -r <repository> -t <token>`
- Output: 
`projects.csv`
- Repository Project (Classic) Output Format: `<number>,<name>,<body>,<state>`
- Log File: 
`projects.log`

### Additional Notes
- The name of the output CSV files can be changed in settings.py
- API endpoint can be changed in settings.py for GitHub Enterprise Server
