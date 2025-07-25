# 🌦️ **Weather Comparison App**

> **A blazing-fast, visually stunning web app to compare weather stats between two cities.**  
> Powered by **FastAPI**, **Chart.js**, and **AWS S3**.

---

## 🚀 **Features**

- 🌍 **Compare** historical weather data for **any 2 cities**
- 📅 **Select date range** (up to 7 days)
- 📊 **Interactive charts** for:
    - Max/Min Temperature
    - Wind Speed
    - Rainy Days
- ☁️ **Save & load** data from **Amazon S3**
- 📂 **Browse saved history** (CSV keys from S3)
- 📥 **Export results** as CSV
- 💡 Built with **FastAPI**, **Jinja2**, **Pandas**, **Boto3**

---

## 📁 **Project Structure**

```plaintext
weather-compare-app/
│
├── main.py              # 🚀 FastAPI app
├── templates/           # 🖼️ Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   └── contact.html
├── static/              # 🎨 CSS & JS
│   └── style.css
├── weather/             # 🌦️ App logic
│   ├── weather_fetcher.py   # ↔️ Weather API
│   └── s3_utils.py          # ☁️ S3 utilities
├── .env                 # 🔐 Secrets (ignored)
├── .gitignore           # 🚫 Ignore rules
├── requirements.txt     # 📦 Dependencies
└── README.md            # 📖 Docs
```

> **Tips:**  
> - Keep your `.env` file **private**!  
> - Templates & static files are **auto-loaded**.  
> - Modular code in `weather/` keeps things **clean & testable**.

---

## 🛠️ **Quick Start**

### 1️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

### 2️⃣ **Create your `.env` file**

```ini
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=your-region
S3_BUCKET_NAME=your-bucket-name
WEATHER_API_KEY=your-weatherapi-key
```

### 3️⃣ **Run the app**

```bash
uvicorn main:app --reload
```
Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 **Tech Stack**

| Backend   | Frontend         | Cloud      | Data      | Weather API      |
|-----------|------------------|------------|-----------|------------------|
| FastAPI   | Jinja2, Chart.js | AWS S3     | Pandas    | weatherapi.com   |

---

## 🗃️ **Example S3 Folder Structure**

```plaintext
kkgbucket4121/
└── weather/
        ├── kolkata_2025-07-24_2025-07-22.csv
        ├── delhi_2025-07-24_2025-07-22.csv
        └── ...
```

---

## ✨ **Screenshots**

_Add your screenshots or GIFs here to showcase the app UI!_

---

## 👤 **About Me**

**Kamal Krishna Ghosh**  
🎓 Full Stack Dev | 🐍 Python + FastAPI Enthusiast  
📧 [kamalkrishnaghosh999@gmail.com](mailto:kamalkrishnaghosh999@gmail.com)

---

## 📄 **License**

This project is **free for learning, demos, and non-commercial use**.  
For commercial use, please contact the author.

---

## ✅ **To Finalize**

- Replace:
    - `your-access-key`, `your-region`, etc.
    - Screenshot URLs
    - Add GitHub/LinkedIn links
- Add `.env` to `.gitignore`
- Push to GitHub:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/yourusername/weather-compare-app.git
    git push -u origin main
    ```

---

## 🌟 **Contributing**

We welcome contributions!  
1. **Fork** the repo  
2. **Create a branch** (`git checkout -b feature/YourFeature`)  
3. **Commit** your changes  
4. **Push** to your branch  
5. **Open a pull request**

---

## 📚 **Resources**

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Chart.js Docs](https://www.chartjs.org/docs/)
- [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [weatherapi.com](https://www.weatherapi.com/)

---

## 🙏 **Acknowledgements**

- Inspired by open weather data projects & the Python open-source community.
- Thanks to all contributors and users!

---

## 📢 **Contact**

For questions, suggestions, or feedback:  
Open an issue or email [kamalkrishnaghosh999@gmail.com](mailto:kamalkrishnaghosh999@gmail.com).

---