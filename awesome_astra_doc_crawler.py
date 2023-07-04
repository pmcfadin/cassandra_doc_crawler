import os
import requests
import yaml


def load_config(config_file):
    with open(config_file, 'r') as stream:
        config = yaml.safe_load(stream)
    return config


def download_md_files(token, repo, path, output_directory):
    headers = {'Authorization': f'token {token}'}
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {r.status_code}")
        return

    files = r.json()

    for file in files:
        if file['type'] == 'dir':
            download_md_files(token, repo, file['path'], output_directory)
        else:
            if file['name'].endswith('.md'):
                download_file(file['download_url'], file['name'], output_directory)


def download_file(url, filename, output_directory):
    r = requests.get(url)
    with open(os.path.join(output_directory, filename), 'w', encoding='utf-8') as file:
        file.write(r.text)
    print(f"Downloaded {filename}")


if __name__ == "__main__":
    config = load_config('awesome_astra_doc_crawler_config.yaml')
    github_config = config['github']
    output_directory = config['output']['directory']

    # Create the output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_md_files(github_config['token'], github_config['repo'], github_config['path'], output_directory)
