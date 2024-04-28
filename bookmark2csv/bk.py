import csv
from bs4 import BeautifulSoup
from datetime import datetime

def convert_datetime(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def parse_bookmarks(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    bookmarks = []

    def process_folder(folder, parent_folder=None):
        if folder is None:
            return []

        sub_bookmarks = []
        for item in folder.find_all(['dt', 'a']):
            if item.name == 'dt':
                folder_name = item.h3.get_text(strip=True) if item.h3 else None
                sub_folder = process_folder(item.dl, folder_name)
                sub_bookmarks.extend(sub_folder)
            elif item.name == 'a':
                url = item['href']
                title = item.get_text(strip=True)
                add_date = convert_datetime(item.get('add_date', '0'))
                sub_bookmarks.append({
                    'Title': title,
                    'URL': url,
                    'Date Added': add_date,
                    'Folder': folder_name,
                    'Parent Folder': parent_folder
                })

        return sub_bookmarks

    bookmarks = process_folder(soup.dl)
    return bookmarks

# Read the HTML content from the file
with open('bookmarks.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the bookmarks and convert to a list of dictionaries
bookmark_data = parse_bookmarks(html_content)

# Write the data to a CSV file
with open('bookmarks.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'URL', 'Date Added', 'Folder', 'Parent Folder']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(bookmark_data)
