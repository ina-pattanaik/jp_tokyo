# 🚀 Selenium UI Automation Project for a sample e-commerce website – Usage Guide

## Prerequisites

- Python 3.7+ installed
- `pip` installed
- At least one supported browser (Chrome, Firefox, or Edge)
- *(Recommended)* Use a virtual environment for Python dependencies

---

## 📂 Project Structure

```
jp_tokyo/
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

## 📝 Design Explanation

### Page Object Model (`pages/demoblaze_pages.py`)

- All DOM interactions (clicks, form fills, alerts) are encapsulated as methods.
- Both positive and negative flows are implemented as methods (e.g., `signup`, `login`, `add_products_to_cart`, `login_negative`, `signup_negative`).
- This abstraction makes the test code clean and maintainable; any UI change is handled in one place.

### Config-Driven (`testparams.json`, `utils/config.py`)

- All environment-specific or variable data (URL, product count, wait times) are in JSON.
- The config loader (`TestConfig`) makes these available as attributes in tests and page objects.

### Reusable Waits (`utils/waits.py`)

- All waits are explicit, using Selenium’s `WebDriverWait` and `expected_conditions`.
- No `time.sleep()` is used, making tests fast and reliable.

### Test Cases (`tests/test_demoblaze.py`)

- Each test case is a method, named for the scenario it covers.
- Positive and negative scenarios are both covered.
- All test logic is in the test class; all UI logic is in the page object.

### Pytest Fixtures

- `driver` fixture handles browser setup/teardown.
- `setup_class` fixture initializes page objects, user data, and config for each test class.

### HTML Reporting

- `pytest-html` plugin generates a detailed, portable HTML report after each run.


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

### 📊 Sample Test Report

![Sample Test Report](https://github.com/ina-pattanaik/jp_tokyo/raw/main/sample_reports/sample_report.png)

---

## ✅ Test Cases

| Test Case ID | Precondition       | Steps                                  | Expected Result                              |
|--------------|--------------------|----------------------------------------|---------------------------------------------|
| TC01         | Site accessible     | Sign up with new username/password     | Success alert, user registered               |
| TC02         | User signed up      | Login with correct credentials         | User logged in, welcome displayed            |
| TC03         | User logged in      | Add 3 different products to cart       | Products added, alert shown each time        |
| TC04         | Products in cart    | Go to cart page                        | All added products listed                    |
| TC05         | Cart has products   | Delete one product from cart           | Product removed, cart updates                |
| TC06         | N/A                 | Sign up with only username             | Error alert shown                            |
| TC07         | N/A                 | Sign up with only password             | Error alert shown                            |
| TC08         | N/A                 | Login with wrong username              | Error alert shown                            |
| TC09         | Existing user       | Login with wrong password              | Error alert shown                            |
| TC10         | N/A                 | Login with wrong username & password   | Error alert shown                            |


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

