# Reddit Scraper & Data Cleaner

A comprehensive web application that combines Reddit scraping and data cleaning functionality in a single, user-friendly Streamlit interface.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

### 🔍 Reddit Scraper
- **Subreddit Selection**: Scrape any public subreddit
- **Multiple Sorting Options**: `new`, `hot`, `top`, or `controversial` posts
- **Time Filters**: Filter by `day`, `week`, `month`, `year`, or `all` time
- **Flexible Post Limits**: Scrape 1-1000 posts (customizable)
- **Keyword Filtering**: Filter posts by keywords in title, content, or comments
- **Real-time Progress**: Live progress tracking during scraping
- **Multiple Export Formats**: JSON (raw data) and cleaned text

### 🧹 Data Cleaner
- **File Upload**: Easy JSON file upload interface
- **Data Validation**: Automatic validation of JSON structure
- **Clean Formatting**: Convert JSON to human-readable text
- **Preview Capability**: Review data before processing
- **Instant Download**: Export cleaned data as text files

## 🚀 Quick Start

### Option 1: Automated Setup
```bash
# Clone the repository
git clone https://github.com/your-username/reddit-scraper.git
cd reddit-scraper

# Run setup script
python setup.py

# Follow the prompts to configure your API credentials
# Then run the app
python -m streamlit run app.py
```

### Option 2: Manual Setup
```bash
# Clone and navigate
git clone https://github.com/your-username/reddit-scraper.git
cd reddit-scraper

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your Reddit API credentials

# Run the application
python -m streamlit run app.py
```

### Option 3: One-Click Launch (Windows)
```bash
# Double-click run_app.bat
run_app.bat
```

## 🔧 Setup Instructions

### 1. Reddit API Credentials

You need Reddit API credentials to use the scraper:

1. **Create a Reddit App**:
   - Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
   - Click "Create App" or "Create Another App"
   - Choose **"script"** as the app type
   - Fill in the required fields:
     - **Name**: Your app name
     - **Description**: Brief description
     - **Redirect URI**: `http://localhost:8080` (required but not used)

2. **Get Your Credentials**:
   - **Client ID**: Found under your app name (short string)
   - **Client Secret**: The longer string labeled "secret"

### 2. Environment Configuration

Create a `.env` file in the project directory:

```env
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here  
USER_AGENT=script:your-app-name:v1.0 (by u/your_username)
```

**Important**: Never commit your `.env` file to version control!

### 3. Installation

```bash
# Install Python dependencies
pip install -r requirements.txt
```

## 📖 Usage Guide

### Web Interface

1. **Start the app**: `python -m streamlit run app.py`
2. **Open browser**: Navigate to `http://localhost:8501`
3. **Choose functionality**: Use sidebar to select "Reddit Scraper" or "Data Cleaner"

### Reddit Scraper Interface

1. **Basic Settings**:
   - Enter subreddit name (without "r/")
   - Choose sort method (`new`, `hot`, `top`, `controversial`)
   - Set number of posts (1-1000)

2. **Advanced Options**:
   - Add time filter for `top`/`controversial` posts
   - Enter keywords for content filtering
   - Review your selections

3. **Scraping & Download**:
   - Click "Start Scraping"
   - Monitor real-time progress
   - Download results as JSON or cleaned text

### Data Cleaner Interface

1. **Upload**: Choose a JSON file from the Reddit scraper
2. **Review**: Check data summary and preview
3. **Clean**: Process the data into readable format
4. **Download**: Export as formatted text file

### Command Line Interface

The original CLI scripts are still available:

```bash
# CLI Scraper
python scraper-main.py

# CLI Data Cleaner  
python data-cleaner.py
```

## 📁 Project Structure

```
reddit-scraper/
├── app.py                      # Main Streamlit application
├── scraper-main.py            # CLI scraper script  
├── data-cleaner.py            # CLI data cleaner
├── setup.py                   # Automated setup script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── .env                      # Your credentials (gitignored)
├── .gitignore               # Git ignore rules
├── run_app.bat              # Windows launcher
├── run_app.sh               # Unix launcher  
└── README.md                # This file
```

## 🔒 Security & Privacy

- **Environment Variables**: API credentials are stored in `.env` file
- **Git Protection**: `.env` is automatically gitignored
- **No Data Storage**: App doesn't store your scraped data
- **Local Processing**: All data processing happens locally

## 🐛 Troubleshooting

### Common Issues

**"Missing Reddit API Credentials"**
- Ensure `.env` file exists with valid credentials
- Check that credentials are not wrapped in quotes
- Verify CLIENT_ID and CLIENT_SECRET are correct

**"Subreddit not found"**  
- Check subreddit name spelling
- Ensure subreddit is public
- Try a different subreddit

**"Rate limit exceeded"**
- Reddit API has rate limits
- Reduce number of posts
- Wait a few minutes between requests

**App won't start**
- Ensure Python 3.7+ is installed
- Install dependencies: `pip install -r requirements.txt`
- Check if port 8501 is available

### Performance Tips

- **Large scrapes**: Expect longer processing times for 500+ posts
- **Keyword filtering**: Reduces processing time by filtering early
- **Comment loading**: Disable comment scraping for faster results

## 🚀 Deployment Options

### Streamlit Cloud
1. Push code to GitHub (ensure `.env` is gitignored)
2. Connect repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add environment variables in Streamlit Cloud settings
4. Deploy with one click

### Heroku
```bash
# Add Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Set environment variables
heroku config:set CLIENT_ID=your_client_id
heroku config:set CLIENT_SECRET=your_client_secret  
heroku config:set USER_AGENT=your_user_agent

# Deploy
git push heroku main
```

### Local Network Access
```bash
# Run on all network interfaces
streamlit run app.py --server.address=0.0.0.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

- **Respect Reddit's Terms**: Use responsibly and respect Reddit's API terms of service
- **Rate Limiting**: Be mindful of API rate limits to avoid being blocked
- **Content Policy**: Ensure scraped content complies with applicable laws and policies
- **Personal Use**: This tool is intended for personal, educational, and research purposes

## 🙋‍♂️ Support

- **Documentation**: Check this README and the inline help
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions

## 🎯 Roadmap

- [ ] Support for multiple subreddits in one operation
- [ ] Advanced filtering options (user, score thresholds)
- [ ] Data visualization dashboard
- [ ] Export to different formats (CSV, Excel)
- [ ] Scheduled scraping capabilities
- [ ] User authentication for personal Reddit data

---

**Happy Scraping!** 🎉