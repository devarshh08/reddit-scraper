# 🤖 Reddit Scraper & Data Cleaner

<div align="center">

**A powerful web application for scraping Reddit data and cleaning it for analysis**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://screddit.streamlit.app/)

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg?style=flat-square)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-FF4B4B.svg?style=flat-square)
![PRAW](https://img.shields.io/badge/praw-v7.7+-orange.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/yourusername/reddit-scraper?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/reddit-scraper?style=flat-square)

</div>

---

## 📋 Table of Contents
- [🎯 Try It Live](#-try-it-live)
- [🌟 Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [🔧 Installation](#-installation)
- [📖 Usage Guide](#-usage-guide)
- [🏗️ Architecture](#️-architecture)
- [🚀 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Try It Live

**👉 [Launch the App on Streamlit Cloud](https://screddit.streamlit.app/) 👈**

*No installation required! Try all features instantly in your browser.*

<div align="center">

### 📱 App Preview

<!-- Add screenshots here when available -->
*Screenshots coming soon! For now, [try the live demo](https://screddit.streamlit.app/)*

</div>

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🔍 Reddit Scraper
- ✅ **Any Public Subreddit** - Scrape from any accessible community
- 📈 **Multiple Sort Methods** - `hot`, `new`, `top`, `controversial`
- ⏰ **Time Filtering** - `day`, `week`, `month`, `year`, `all time`
- 🔢 **Flexible Limits** - 1 to 1,000 posts per scrape
- 🔎 **Keyword Filtering** - Target specific content
- 📉 **Real-time Progress** - Live scraping updates
- 📥 **Multiple Formats** - JSON + cleaned text export
- 💬 **Full Comments** - Including nested replies

</td>
<td width="50%">

### 🧹 Data Cleaner
- 📁 **Drag & Drop Upload** - Easy file handling
- ✅ **Auto Validation** - Smart JSON structure checking
- 📝 **Human Readable** - Convert to clean text format
- 👀 **Preview Mode** - Review before processing
- ⚡ **Instant Export** - One-click download
- 📈 **Data Insights** - Post/comment statistics
- 🎨 **Clean Formatting** - Structured, readable output
- 🚀 **Fast Processing** - Optimized for large datasets

</td>
</tr>
</table>

## 🎯 Use Cases

<div align="center">

| 🎨 **Content Research** | 📈 **Market Analysis** | 🎓 **Academic Study** | 🤖 **AI Training** |
|:---:|:---:|:---:|:---:|
| Gather content ideas | Analyze brand mentions | Research social trends | Collect training data |
| Study engagement patterns | Monitor competitor discussions | Study online communities | Build sentiment datasets |
| Find trending topics | Track product feedback | Analyze discourse patterns | Create conversation datasets |

</div>

## 🚀 Quick Start

### 🌐 Option 1: Use Online (Recommended)
```
👉 Just visit: https://screddit.streamlit.app/
✅ No installation needed
✅ No API setup required
✅ Works on any device
```

### 💻 Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/your-username/reddit-scraper.git
cd reddit-scraper

# Quick setup
python setup.py

# Launch app
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

## 🏗️ Tech Stack

<div align="center">

| **Frontend** | **Backend** | **APIs** | **Deployment** |
|:---:|:---:|:---:|:---:|
| 📊 Streamlit | 🐍 Python 3.7+ | 🔴 Reddit API (PRAW) | ☁️ Streamlit Cloud |
| 📋 HTML/CSS | 📦 JSON Processing | 🔑 OAuth 2.0 | 🐳 Docker Ready |
| ⚡ Real-time Updates | 🧮 Data Cleaning | 🔒 Secure Secrets | 🌍 HTTPS |

</div>

## 📎 Architecture

```
🏗️ reddit-scraper/
├── 🚀 app.py                      # Main Streamlit application
├── ⚙️  scraper-main.py            # CLI scraper script  
├── 🧹 data-cleaner.py            # CLI data cleaner
├── 🔧 setup.py                   # Automated setup script
├── 📦 requirements.txt           # Python dependencies
├── 🔑 .streamlit/secrets.toml    # Secure credentials
├── 📝 .env.example              # Environment template
├── ⚙️  .gitignore                 # Git ignore rules
├── 💻 run_app.bat              # Windows launcher
├── 🐧 run_app.sh               # Unix launcher  
└── 📝 README.md                # Documentation
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

## 🚀 Deployment

### 🌐 Streamlit Cloud (Current Deployment)

**✅ Live at: [screddit.streamlit.app](https://screddit.streamlit.app/)**

To deploy your own instance:

1. **Fork this repository**
2. **Connect to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your forked repository

3. **Configure Secrets** (in Advanced Settings):
   ```toml
   CLIENT_ID = "your_reddit_client_id"
   CLIENT_SECRET = "your_reddit_client_secret"
   USER_AGENT = "script:your-app-name:v1.0 (by u/your_username)"
   ```

4. **Deploy** - Streamlit handles the rest!

### 🐳 Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### 🔗 Other Platforms
- **Heroku**: Add `Procfile` and config vars
- **Railway**: Connect GitHub and deploy
- **Render**: Deploy with automatic builds

## 🤝 Contributing

We love your input! We want to make contributing as easy and transparent as possible.

### Ways to Contribute
- 🐛 **Report bugs** - Create detailed issue reports
- ✨ **Suggest features** - Share your ideas for improvements  
- 📝 **Improve docs** - Help make our documentation better
- 💻 **Submit code** - Fix bugs or add new features

### Development Process
1. 🍴 **Fork** the repository
2. 🌱 **Create** your feature branch: `git checkout -b feature/amazing-feature`
3. ✨ **Make** your changes with clear, descriptive commits
4. ✅ **Test** your changes thoroughly
5. 📤 **Push** to your branch: `git push origin feature/amazing-feature`
6. 📩 **Open** a Pull Request with a clear description

### Code Style
- Follow PEP 8 for Python code
- Add docstrings to new functions
- Include type hints where appropriate
- Write clear commit messages

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

<div align="center">

## 🏷️ GitHub Topics

`reddit` `scraper` `data-mining` `streamlit` `python` `praw` `web-app` `data-analysis` `social-media` `json` `data-cleaning` `reddit-api` `streamlit-app` `web-scraping` `data-science`

---

### 💖 Show Your Support

If this project helped you, please ⭐ **star the repository** and share it with others!

[![GitHub stars](https://img.shields.io/github/stars/yourusername/reddit-scraper?style=social)](https://github.com/yourusername/reddit-scraper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/reddit-scraper?style=social)](https://github.com/yourusername/reddit-scraper/network/members)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fyourusername%2Freddit-scraper)](https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20Reddit%20scraper%20and%20data%20cleaner!&url=https://github.com/yourusername/reddit-scraper)

---

### 🔗 Quick Links

[🌐 **Live Demo**](https://screddit.streamlit.app/) | [📝 **Documentation**](#-table-of-contents) | [🐛 **Report Bug**](https://github.com/yourusername/reddit-scraper/issues) | [✨ **Request Feature**](https://github.com/yourusername/reddit-scraper/issues)

---

**Built with ❤️ by [Your Name](https://github.com/yourusername)**

**Happy Scraping!** 🎉

</div>
