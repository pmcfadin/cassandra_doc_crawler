# CassandraDocSpider

CassandraDocSpider is a crawler script written in Python, specifically built to crawl Apache Cassandra documentation available online. It uses Scrapy, an open-source and collaborative web crawling framework for Python, to navigate through the website and download the required data. The script takes care of excluding specified URL patterns while crawling.

## Prerequisites

To run this project, you need to have:

- Python (version 3.7 or later)
## Quick Start

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yourgithubusername/CassandraDocSpider.git
cd CassandraDocSpider
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
Modify the deny_list if needed

```python
deny_list = ['https://www.apache.org', 'https://cassandra.apache.org/_/blog/',
             'https://cassandra.apache.org/_/case-studies', 'https://cassandra.apache.org/doc/3.11']
```
You may also change the start_url and output_dir variables, which represent the starting point for the crawler and the output directory for the crawled data, respectively.
```python
process.crawl(CassandraDocSpider, start_url='https://cassandra.apache.org/doc/latest/',
              output_dir='output/cassandra_docs', deny_list=deny_list)
```
After setting up the script, run it from the terminal using the command:
```bash
python cassandradoccrawler.py
```
The script will start the crawling process and save the downloaded data in the specified output directory.


# Markdown File Downloader
## Description
This tool helps you download all Markdown (.md) files from the awesome-astra GitHub repository.

## How It Works
The tool makes use of the GitHub API to fetch file information and download files. It uses the requests and os libraries in Python, and the configuration is managed using YAML files.

## Installation
No specific installation is required. Just clone this repository to your local machine.

## Requirements
The tool requires the following Python packages which can be installed using pip:

requests
PyYAML

You can install these dependencies with:

```bash
pip install requests pyyaml
```
## Usage
First, prepare your configuration YAML file. A template is provided below:

```yaml

github:
  token: "your_github_token_here"
  repo: "username/repo"
  path: "directory_in_repo"
output:
  directory: "your_output_directory_here"
```

Make sure to replace "your_github_token_here" with your personal GitHub token, "username/repo" with the repository you are targeting, "directory_in_repo" with the directory you want to target in the repository, and "your_output_directory_here" with the path where you want to save the downloaded Markdown files.

After preparing your YAML file, run the script as follows:

```bash
python main.py
```
The script will read the YAML configuration file, fetch the file metadata from GitHub and download all the Markdown files found in the specified directory, saving them to your specified output directory. If a targeted sub-directory is found, the tool will recursively search and download from those as well.

## Error Handling
If any error occurs during the fetch operation, such as an invalid token or inaccessible repository, an error message with the respective HTTP status code will be printed.