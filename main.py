from bs4 import BeautifulSoup
import os

def extract_usernames_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        usernames = [a.text.strip() for a in soup.find_all('a')]
        return set(usernames)

# 👉 Replace with actual path if not in same folder
followers_files = ['followers_1.html']  # Add more if you have
following_file = 'following.html'

# 👤 Load followers
followers = set()
for ffile in followers_files:
    followers.update(extract_usernames_from_html(ffile))

# 👀 Load following
following = extract_usernames_from_html(following_file)

# 🐍 People you follow but who don't follow back
not_following_back = following - followers

# 💔 Output the truth
print("People who don't follow you back:")
for user in sorted(not_following_back):
    print(user)