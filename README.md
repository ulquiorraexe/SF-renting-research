# SF Renting Research Automation

## Description

SF Renting Research Automation is a Python script that extracts rental property data (address, price, and links) from a Zillow clone website and inputs the data into a Google Form for research purposes. The script uses web scraping with BeautifulSoup and automates form submissions using Selenium.

## Features

- Scrapes rental property details such as addresses, prices, and links from the given website.
- Automates data entry into a Google Form.
- Uses BeautifulSoup for web scraping and Selenium for browser automation.
- Supports the automation of repetitive tasks.

## Installation

To run this project locally, follow the steps below:

1. **Clone the repository:**

    ```bash
    gh repo clone ulquiorraexe/SF-renting-research
    ```

2. **Install the required libraries:**

    This project uses `requests`, `beautifulsoup4`, `selenium`, and `lxml` for web scraping and automation. Install them using pip:

    ```bash
    pip install requests beautifulsoup4 selenium lxml
    ```

3. **Install ChromeDriver:**

    - If you're using Chrome, download ChromeDriver from the following link:
    [ChromeDriver Download](https://sites.google.com/chromium.org/driver/)
    
    - Make sure that the version of ChromeDriver matches the version of Google Chrome installed on your machine.

4. **Set up the necessary environment:**

    Ensure that you have a working Chrome installation and the necessary permissions to run automated browsers.

## Usage

### Steps to Run the Script

1. **Run the Python script:**

    Execute the Python script to scrape the Zillow clone website and submit the data to the Google Form.

    ```bash
    python main.py
    ```

2. **The script will:**
    - Open the Zillow clone website and extract property information.
    - Open a Google Form and input the scraped data for each property.
    - Automate the form submissions for each property.

    The script will repeat this process for all properties found on the website.

## Notes

- **Web Scraping**: The script scrapes property details such as address, price, and links from a Zillow clone website.
- **Google Form Automation**: The script automates the process of filling out a Google Form with the scraped data, simulating user input.
- **Selenium Setup**: Make sure you have the Chrome browser and ChromeDriver installed to enable Selenium's automation features.

## License

This project is not licensed, and no specific license is applied to it. Feel free to use and modify the code as needed.

## Contributing

If you would like to contribute to the project, feel free to fork the repository, make changes, and create a pull request with improvements or fixes.

