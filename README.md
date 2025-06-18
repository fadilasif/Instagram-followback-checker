🕵️‍♂️ Instagram Follow Checker

Uncover the cold, hard truth about who’s not following you back on Instagram. This slick Python script slices through your Instagram data export like a digital ninja, using BeautifulSoup to parse HTML files and expose those one-sided follows. No API nonsense, just pure, unfiltered username extraction.

🚀 Prerequisites

Python 3.x (because who’s still on 2.x, honestly?).
BeautifulSoup4:pip install beautifulsoup4


A dash of patience to deal with Instagram’s data export process.


🛠️ How to Use
Step 1: Snag Your Instagram Data

Fire up Instagram (app or browser, your call).
Navigate to Settings > Your activity > Download your information.
Request a data download in HTML format. Make sure to check "Followers and Following."
Wait for Instagram’s email with the download link—this could take hours or even a day, because apparently they’re still using carrier pigeons.
Unzip the downloaded file and find the followers_and_following folder. You’ll see:
followers_1.html (or similar, listing your followers).
following.html (the accounts you’re following).



Step 2: Prep the Script

Drop the script (find_non_followers.py) into the same folder as your followers_1.html and following.html files.
Got multiple follower files (e.g., followers_1.html, followers_2.html)? Update the followers_files list in the script:followers_files = ['followers_1.html', 'followers_2.html']  # Add all follower files here


Confirm following_file is set to following.html:following_file = 'following.html'



Step 3: Run It Like You Mean It

Open your terminal and cd to the script’s directory.
Unleash the script:python find_non_followers.py


Watch as it spits out a neatly sorted list of users you follow who don’t return the love.


🔍 What It Does

Input: HTML files (followers_*.html, following.html) from your Instagram data export.
Magic:
BeautifulSoup rips usernames from <a> tags in the HTML.
Compares your following set against your followers set.
Outputs the betrayers—users you follow who don’t follow you back.


Output: A clean, alphabetical list of usernames printed to your console.


📜 Example Output
People who don't follow you back:
sneaky_user123
ghostly_vibes
why_even_bother


💡 Pro Tips

File Paths: If your HTML files aren’t in the same folder as the script, update the paths in the code or move the files. Don’t make the script hunt for them.
Multiple Follower Files: Instagram might split your followers into multiple files. Add them all to followers_files to avoid missing anyone.
No API, No Drama: This script sidesteps Instagram’s API entirely, so you’re free from rate limits or auth headaches.
Data Privacy: Your Instagram data export contains sensitive info. Keep it secure and don’t share it with randos.


🐛 Troubleshooting

FileNotFoundError: Double-check that your HTML files are in the right folder and their names match what’s in the script.
Empty Output: Ensure your HTML files aren’t empty or corrupted. Instagram’s export can be finicky.
Encoding Issues: The script assumes UTF-8. If you hit weird character errors, verify your HTML files’ encoding.


⚠️ Disclaimer
This is for personal use only. Don’t be a creep—respect Instagram’s terms and other users’ privacy. Using this to spam or harass is a one-way ticket to bad karma.

🌟 Why This Script Slaps
It’s lightweight, doesn’t need an internet connection after you’ve got the files, and cuts through the noise to deliver the truth. Who’s got time for fake followers? Not you.
