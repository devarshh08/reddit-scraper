import praw
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from tqdm import tqdm

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

def scrape_subreddit(subreddit_name, limit=10, sort="new", time_filter="all", keywords=None):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        check_for_async=False
    )

    sub = reddit.subreddit(subreddit_name)

    if sort == "new":
        submissions = sub.new(limit=limit)
    elif sort == "hot":
        submissions = sub.hot(limit=limit)
    elif sort == "top":
        submissions = sub.top(time_filter=time_filter, limit=limit)
    else:
        submissions = sub.controversial(time_filter=time_filter, limit=limit)

    results = []

    print(f"\nScraping {limit} posts from r/{subreddit_name} sorted by {sort}...\n")
    for submission in tqdm(submissions, desc="Posts", unit="post"):
        submission.comments.replace_more(limit=None)
        comments = []
        for comment in submission.comments.list():
            comments.append({
                "id": comment.id,
                "parent_id": comment.parent_id,
                "body": comment.body,
                "author": str(comment.author) if comment.author else None,
                "score": comment.score,
            })

        item = {
            "id": submission.id,
            "title": submission.title,
            "author": str(submission.author) if submission.author else None,
            "score": submission.score,
            "num_comments": submission.num_comments,
            "created_utc": int(submission.created_utc),
            "created_iso": datetime.utcfromtimestamp(submission.created_utc).isoformat() + "Z",
            "selftext": submission.selftext,
            "url": submission.url,
            "comments": comments,
        }

        if keywords:
            text_to_search = (submission.title + " " + submission.selftext + " " +
                              " ".join([c["body"] for c in comments]))
            if not any(kw.lower() in text_to_search.lower() for kw in keywords):
                continue

        results.append(item)

    return results

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name (without r/): ").strip()

    sort_choice = input("Choose sorting method (hot/new/top): ").strip().lower()
    if sort_choice not in ["hot", "new", "top"]:
        sort_choice = "new"

    limit_input = input("How many posts do you want to fetch? (press Enter for max 1000): ").strip()
    if limit_input == "":
        limit = 1000
    elif limit_input.isdigit():
        limit = min(int(limit_input), 1000)
    else:
        limit = 10

    keywords_input = input("Enter keywords to filter (comma separated, leave empty for none): ").strip()
    if keywords_input:
        keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
    else:
        keywords = None

    data = scrape_subreddit(subreddit_name, limit=limit, sort=sort_choice, keywords=keywords)

    out_file = f"{subreddit_name}_{sort_choice}_output.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Scraping complete! Saved {len(data)} posts to {out_file}")