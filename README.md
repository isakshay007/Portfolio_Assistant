# Investment Portfolio Management Assistant 🚀

## Overview
The **Investment Portfolio Management Assistant** is a Streamlit-based application designed to simplify the creation and management of investment portfolios. Powered by **Lyzr Automata SDK**, this app analyzes policyholder data, reviews policy specifics, and ensures compliance with regulatory requirements to develop optimized investment portfolios and generate comprehensive performance reports.

---

## Features
- **Policyholder Data Analysis**:
  - Analyzes data such as age, gender, health status, premium amount, term of the policy, and sum assured.
- **Regulatory Compliance**:
  - Ensures portfolios align with current legal standards and practices.
- **Investment Portfolio Creation**:
  - Develops diversified and risk-managed investment portfolios tailored to individual policyholder needs.
- **Performance Reporting**:
  - Generates detailed performance reports with future trend forecasts and strategic recommendations.
- **Interactive User Input**:
  - Accepts detailed policyholder information via a user-friendly input field.

---

## Installation

### Prerequisites
- **Python**: Ensure Python 3.8 or higher is installed.
- **Dependencies**: Install required packages via `requirements.txt`.
- **API Keys**: Obtain the following keys:
  - **OpenAI API Key**

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/investment-portfolio-assistant.git
   cd investment-portfolio-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API Key:
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add your API key:
     ```toml
     [apikey]
     apikey = "your_openai_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Usage

1. **Input Policyholder Information**:
   - Provide policyholder details, premium amount, term of the policy, sum assured, and regulatory requirements in the input field.
2. **Generate Portfolio**:
   - Click the "Generate!" button to create an investment portfolio and a performance report.
3. **Review Results**:
   - The generated portfolio and report will be displayed in Markdown format.

---

## File Structure
```
investment-portfolio-assistant/
│
├── app.py                  # Main application file
├── logo/                   # Directory for logo assets
│   ├── lyzr-logo.png
├── requirements.txt        # Python dependencies
└── .streamlit/             # Streamlit configuration
    └── secrets.toml        # API key configuration
```

---

## Key Functionalities

### 1. **Data Analysis**
- Gathers and organizes policyholder data to inform investment decisions.

### 2. **Portfolio Creation**
- Constructs optimized portfolios based on individual policy specifics and regulatory standards.

### 3. **Performance Reporting**
- Generates detailed reports reflecting portfolio status, future trends, and strategic recommendations.

---

## Dependencies
- **Streamlit**: Interactive UI framework.
- **Lyzr Automata SDK**: AI-powered portfolio generation and analysis.
- **Pillow**: For handling image assets.
- **Python (>=3.8)**

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments
- Built using the **Lyzr Automata SDK**.
- Designed to assist in streamlined investment portfolio management.

---
