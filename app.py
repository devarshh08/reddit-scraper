import streamlit as st
import praw
import json
import os
from datetime import datetime
from tqdm import tqdm
import io
import time
from dotenv import load_dotenv

# Load environment variables (try multiple paths)
load_dotenv()  # Try current directory first
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))  # Try script directory

# Page config
st.set_page_config(
    page_title="Reddit Scraper & Data Cleaner",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Reddit API credentials from environment
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# Debug info (remove this after testing)
# st.write(f"Debug - Current working directory: {os.getcwd()}")
# st.write(f"Debug - Script directory: {os.path.dirname(__file__)}")
# st.write(f"Debug - CLIENT_ID loaded: {bool(CLIENT_ID)}")

# Check if credentials are loaded
if not all([CLIENT_ID, CLIENT_SECRET, USER_AGENT]):
    st.error(f"""
    ⚠️ **Missing Reddit API Credentials**
    
    **Debug Information:**
    - Current working directory: `{os.getcwd()}`
    - Script directory: `{os.path.dirname(os.path.abspath(__file__))}`
    - .env file exists: `{os.path.exists('.env')}`
    - .env in script dir: `{os.path.exists(os.path.join(os.path.dirname(__file__), '.env'))}`
    
    **Solution:**
    Please ensure a `.env` file exists in your project directory with:
    ```
    CLIENT_ID=your_client_id_here
    CLIENT_SECRET=your_client_secret_here
    USER_AGENT=your_user_agent_here
    ```
    """)
    st.stop()

# Utility Functions
def scrape_subreddit(subreddit_name, limit=10, sort="new", time_filter="all", keywords=None, progress_callback=None):
    """
    Scrape subreddit posts with all available options
    """
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
            check_for_async=False
        )

        sub = reddit.subreddit(subreddit_name)

        # Get submissions based on sort method
        if sort == "new":
            submissions = sub.new(limit=limit)
        elif sort == "hot":
            submissions = sub.hot(limit=limit)
        elif sort == "top":
            submissions = sub.top(time_filter=time_filter, limit=limit)
        elif sort == "controversial":
            submissions = sub.controversial(time_filter=time_filter, limit=limit)
        else:
            submissions = sub.new(limit=limit)

        results = []
        processed = 0

        for submission in submissions:
            processed += 1
            if progress_callback:
                progress_callback(processed, limit)

            # Get comments
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

            # Filter by keywords if provided
            if keywords:
                text_to_search = (submission.title + " " + submission.selftext + " " +
                                  " ".join([c["body"] for c in comments]))
                if not any(kw.lower() in text_to_search.lower() for kw in keywords):
                    continue

            results.append(item)

        return results, None

    except Exception as e:
        return None, str(e)

def format_reddit_data(data):
    """
    Format Reddit JSON data into readable text format
    """
    output = io.StringIO()
    
    for post in data:
        output.write("=" * 60 + "\n")
        output.write(f"POST TITLE: {post.get('title', 'No Title')}\n")
        
        author = post.get('author', 'N/A')
        score = post.get('score', 0)
        num_comments = post.get('num_comments', 0)
        try:
            created_date = datetime.fromisoformat(post.get('created_iso', '...Z').replace('Z', '+00:00')).strftime('%Y-%m-%d')
        except:
            created_date = 'N/A'
        
        output.write(f"Author: {author} | Score: {score} | Comments: {num_comments} | Date: {created_date}\n")
        output.write("-" * 60 + "\n\n")

        if post.get('selftext'):
            output.write(f"{post['selftext']}\n\n")

        if 'comments' in post and post['comments']:
            output.write("--- COMMENTS ---\n\n")
            for comment in post['comments']:
                comment_author = comment.get('author', 'N/A')
                comment_score = comment.get('score', 0)
                comment_body = comment.get('body', '').replace('\n', '\n  ')
                
                output.write(f"Comment by {comment_author} (Score: {comment_score}):\n")
                output.write(f"  {comment_body}\n\n")
        
        output.write("\n" * 2)
    
    return output.getvalue()

# Main App
def main():
    st.title("🤖 Reddit Scraper & Data Cleaner")
    st.markdown("---")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose functionality:", ["Reddit Scraper", "Data Cleaner"])
    
    if page == "Reddit Scraper":
        reddit_scraper_page()
    else:
        data_cleaner_page()

def reddit_scraper_page():
    st.header("📥 Reddit Subreddit Scraper")
    st.markdown("Scrape posts and comments from any subreddit with advanced filtering options.")
    
    # Create columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Basic Settings")
        
        # Subreddit input
        subreddit_name = st.text_input(
            "Subreddit Name (without r/)", 
            placeholder="e.g., python, AskReddit, technology",
            help="Enter the name of the subreddit you want to scrape"
        )
        
        # Sort method
        sort_method = st.selectbox(
            "Sort Method",
            options=["new", "hot", "top", "controversial"],
            help="Choose how to sort the posts"
        )
        
        # Time filter (only for top and controversial)
        time_filter = None
        if sort_method in ["top", "controversial"]:
            time_filter = st.selectbox(
                "Time Filter",
                options=["all", "day", "week", "month", "year"],
                help="Filter posts by time period"
            )
        
        # Number of posts
        limit = st.number_input(
            "Number of Posts",
            min_value=1,
            max_value=1000,
            value=10,
            help="Maximum number of posts to scrape (up to 1000)"
        )
    
    with col2:
        st.subheader("Advanced Options")
        
        # Keywords filtering
        keywords_input = st.text_area(
            "Keywords Filter (Optional)",
            placeholder="python, machine learning, AI\n(one per line or comma-separated)",
            help="Only scrape posts containing these keywords in title, text, or comments"
        )
        
        keywords = None
        if keywords_input.strip():
            # Handle both comma-separated and line-separated keywords
            if ',' in keywords_input:
                keywords = [kw.strip() for kw in keywords_input.split(',') if kw.strip()]
            else:
                keywords = [kw.strip() for kw in keywords_input.split('\n') if kw.strip()]
        
        # Display selected options
        st.subheader("Selected Options")
        st.info(f"""
        **Subreddit:** r/{subreddit_name if subreddit_name else 'Not specified'}
        **Sort:** {sort_method}
        **Time Filter:** {time_filter if time_filter else 'N/A'}
        **Posts:** {limit}
        **Keywords:** {len(keywords) if keywords else 0} keywords
        """)
    
    # Scraping section
    st.markdown("---")
    
    if st.button("🚀 Start Scraping", type="primary", disabled=not subreddit_name):
        if not subreddit_name:
            st.error("Please enter a subreddit name!")
            return
            
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        def update_progress(current, total):
            progress = current / total
            progress_bar.progress(progress)
            status_text.text(f"Processed {current}/{total} posts...")
        
        with st.spinner("Scraping subreddit data..."):
            start_time = time.time()
            data, error = scrape_subreddit(
                subreddit_name=subreddit_name,
                limit=limit,
                sort=sort_method,
                time_filter=time_filter or "all",
                keywords=keywords,
                progress_callback=update_progress
            )
            end_time = time.time()
        
        if error:
            st.error(f"Error occurred during scraping: {error}")
            return
        
        if not data:
            st.warning("No posts found matching your criteria!")
            return
        
        # Success message
        st.success(f"✅ Successfully scraped {len(data)} posts in {end_time - start_time:.2f} seconds!")
        
        # Display results
        st.subheader("📊 Scraping Results")
        
        # Results summary
        total_comments = sum(len(post.get('comments', [])) for post in data)
        avg_score = sum(post.get('score', 0) for post in data) / len(data) if data else 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Posts Scraped", len(data))
        with col2:
            st.metric("Total Comments", total_comments)
        with col3:
            st.metric("Average Score", f"{avg_score:.1f}")
        with col4:
            st.metric("Time Taken", f"{end_time - start_time:.2f}s")
        
        # Preview data
        if st.checkbox("Show preview of scraped data"):
            st.subheader("Data Preview")
            for i, post in enumerate(data[:3]):  # Show first 3 posts
                with st.expander(f"Post {i+1}: {post.get('title', 'No Title')[:50]}..."):
                    st.write(f"**Author:** {post.get('author', 'N/A')}")
                    st.write(f"**Score:** {post.get('score', 0)}")
                    st.write(f"**Comments:** {post.get('num_comments', 0)}")
                    st.write(f"**Content:** {post.get('selftext', 'No content')[:200]}...")
        
        # Download options
        st.subheader("💾 Download Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # JSON download
            json_data = json.dumps(data, ensure_ascii=False, indent=2)
            st.download_button(
                label="📄 Download as JSON",
                data=json_data,
                file_name=f"{subreddit_name}_{sort_method}_output.json",
                mime="application/json"
            )
        
        with col2:
            # Cleaned text download
            cleaned_text = format_reddit_data(data)
            st.download_button(
                label="📝 Download as Cleaned Text",
                data=cleaned_text,
                file_name=f"{subreddit_name}_{sort_method}_cleaned.txt",
                mime="text/plain"
            )

def data_cleaner_page():
    st.header("🧹 Data Cleaner")
    st.markdown("Upload a JSON file from the Reddit scraper and convert it to a clean, readable text format.")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a JSON file",
        type=['json'],
        help="Upload a JSON file generated by the Reddit scraper"
    )
    
    if uploaded_file is not None:
        try:
            # Read and parse JSON
            json_data = json.load(uploaded_file)
            
            # Validate data structure
            if not isinstance(json_data, list):
                st.error("Invalid JSON format. Expected a list of posts.")
                return
            
            if not json_data:
                st.warning("The uploaded JSON file is empty.")
                return
            
            # Display file info
            st.success(f"✅ Successfully loaded JSON file with {len(json_data)} posts!")
            
            # Show data summary
            st.subheader("📊 Data Summary")
            
            total_comments = sum(len(post.get('comments', [])) for post in json_data)
            avg_score = sum(post.get('score', 0) for post in json_data) / len(json_data) if json_data else 0
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Posts", len(json_data))
            with col2:
                st.metric("Total Comments", total_comments)
            with col3:
                st.metric("Average Score", f"{avg_score:.1f}")
            
            # Preview option
            if st.checkbox("Show data preview"):
                st.subheader("Data Preview")
                for i, post in enumerate(json_data[:2]):  # Show first 2 posts
                    with st.expander(f"Post {i+1}: {post.get('title', 'No Title')[:50]}..."):
                        st.json(post)
            
            # Clean data button
            if st.button("🧹 Clean Data", type="primary"):
                with st.spinner("Cleaning data..."):
                    cleaned_text = format_reddit_data(json_data)
                
                st.success("✅ Data cleaned successfully!")
                
                # Show preview of cleaned text
                st.subheader("📄 Cleaned Text Preview")
                st.text_area(
                    "Preview (first 1000 characters)",
                    value=cleaned_text[:1000] + ("..." if len(cleaned_text) > 1000 else ""),
                    height=300,
                    disabled=True
                )
                
                # Download cleaned text
                st.download_button(
                    label="📥 Download Cleaned Text",
                    data=cleaned_text,
                    file_name=f"{uploaded_file.name.replace('.json', '_cleaned.txt')}",
                    mime="text/plain"
                )
                
        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please check the file format.")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")

if __name__ == "__main__":
    main()