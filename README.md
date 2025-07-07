# 🚀 Selenium UI Automation Project – Usage Guide

## Prerequisites

- Python 3.7+ installed
- `pip` installed
- At least one supported browser (Chrome, Firefox, or Edge)
- *(Recommended)* Use a virtual environment for Python dependencies

---

## 📂 Project Structure

```
your_project/
├── conftest.py
├── requirements.txt
├── testparams.json
├── pages/
│   └── demoblaze_pages.py
├── tests/
│   └── test_demoblaze.py
├── utils/
│   ├── helpers.py
│   ├── config.py
│   └── waits.py
└── reports/
    └── report.html
```

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Project

Extract the zip file or clone the repository to your local machine.

```bash
git clone <repository_url>
```

### 2. *(Optional)* Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Test Parameters

Edit `testparams.json` to adjust:

- The target URL
- Number of products to add

#### Example:

```json
{
  "url": "https://www.demoblaze.com/index.html",
  "num_products_to_add": 3,
}
```

---

## 🚀 Running the Tests

### Default (Chrome):

```bash
pytest --html=reports/report.html --self-contained-html
```

### Specify Browser (Chrome, Firefox, or Edge):

```bash
pytest --browser=firefox --html=reports/report.html --self-contained-html
pytest --browser=edge --html=reports/report.html --self-contained-html
```

> **Note:** The correct browser driver will be downloaded automatically.

---

## 📄 Viewing the Test Report

After the test run, open the HTML report in your browser:

### macOS:

```bash
open -a "Google Chrome" reports/report.html
```

### Linux:

```bash
xdg-open reports/report.html
```

### Windows:

Simply double-click `reports/report.html` in your file explorer.

---

## ❓ Troubleshooting

- **Missing browser:** Install the required browser.
- **Driver errors:** Ensure you have internet access for `webdriver-manager` to download drivers.
- **Python errors:** Check your Python version and make sure all dependencies are installed.

---

## 🌟 Project Highlights

- **Page Object Model:** All UI logic is encapsulated in `pages/demoblaze_pages.py`
- **Configurable:** Test parameters are managed in `testparams.json`
- **Robust Waits:** Uses explicit waits for reliable execution (`utils/waits.py`)
- **HTML Reporting:** Clean, portable HTML report generated after each run
- **Cross-platform:** Works on Windows, macOS, and Linux

---

## 🙌 Enjoy Automated Testing!

If you have questions or need further help, just ask.

