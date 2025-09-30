# Reddit Subreddit Scraper

This script lets you download posts and all their comments from any subreddit you choose. It's a simple tool that runs in your terminal and asks you what you want to grab.

---

## What It Can Do

- **No Code Editing Needed:** Just run the script, and it will ask for the subreddit, how you want to sort, and other options.  
- **Sort by Hot, New, or Top:** Pull the posts that are currently popular, the newest ones, or the all-time top posts.  
- **Choose How Many Posts:** You can tell the script exactly how many posts you want to get, up to a maximum of 1000.  
- **Get All Comments:** Downloads every comment on a post, including all nested replies.  
- **Filter by Keywords:** Enter a list of keywords; the script will only save posts where the title, the main text, or any comments include one of those words.  
- **See Your Progress:** A simple progress bar shows how much work has been done and what's left.  
- **Clean JSON Files:** All data is saved in an easy-to-read JSON file, named with the subreddit and the sorting type (like `python_new_output.json`).  

---

## What You'll Need

Make sure you have **Python 3** on your system. You'll also need two packages:

- `praw`: A tool for working with the Reddit API.  
- `tqdm`: Used for the progress bar.  

Install both with:

```bash
pip install praw tqdm
