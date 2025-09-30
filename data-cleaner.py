import json
from datetime import datetime

def format_reddit_data(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{input_file}'. The file might be empty or corrupted.")
        return

    with open(output_file, 'w', encoding='utf-8') as f:
        for post in data:
            f.write("=" * 60 + "\n")
            f.write(f"POST TITLE: {post.get('title', 'No Title')}\n")
            
            author = post.get('author', 'N/A')
            score = post.get('score', 0)
            num_comments = post.get('num_comments', 0)
            created_date = datetime.fromisoformat(post.get('created_iso', '...Z').replace('Z', '+00:00')).strftime('%Y-%m-%d')
            
            f.write(f"Author: {author} | Score: {score} | Comments: {num_comments} | Date: {created_date}\n")
            f.write("-" * 60 + "\n\n")

            if post.get('selftext'):
                f.write(f"{post['selftext']}\n\n")

            if 'comments' in post and post['comments']:
                f.write("--- COMMENTS ---\n\n")
                for comment in post['comments']:
                    comment_author = comment.get('author', 'N/A')
                    comment_score = comment.get('score', 0)
                    comment_body = comment.get('body', '').replace('\n', '\n  ')
                    
                    f.write(f"Comment by {comment_author} (Score: {comment_score}):\n")
                    f.write(f"  {comment_body}\n\n")
            
            f.write("\n" * 2)

    print(f"✅ Data cleaning complete! Formatted data saved to '{output_file}'")

if __name__ == "__main__":
    input_filename = input("Enter the path to the JSON file to clean: ").strip()
    
    if input_filename:
        output_filename = input_filename.replace('.json', '_cleaned.txt')
        format_reddit_data(input_filename, output_filename)
    else:
        print("No file location provided. Exiting.")