<p align="center">
<img src="img/logo.png" width="400" />
</p>
<p align="center">
Automate flight searches and get the best deals effortlessly!
</p>

***


## Description

This Python script utilizes the Selenium library to automate flight search and booking on a travel booking website. The goal of the script is to find the cheapest flight between a specified origin and destination entered by the user.

The automation process involves opening a browser window, inputting the required information into the website's search form, and identifying the lowest price among the obtained results. Additionally, the script can also perform the purchase of the selected flight by clicking on the purchase button.

## Requirements

- Python 3.x
- Selenium library

## Installation Instructions

1. Ensure that you have Python 3.x installed on your system.
2. Install the Selenium library by executing the following command in your terminal:
```bash
pip install selenium
```

3. Download the `flight_search.py` script file from the repository.
4. Make sure you have the corresponding browser driver installed on your system. In the case of Chrome, you need to have the Chrome driver (chromedriver) installed and in your system's PATH.
- You can download the Chrome driver from [here]([https://sites.google.com/a/chromium.org/chromedriver/downloads](https://developer.chrome.com/docs/chromedriver/downloads?hl=it).
- Make sure to download the driver version that corresponds to your Chrome browser version.
- Run the downloaded driver file and ensure that it is in your system's PATH.
5. Modify the URL in the script code, replacing `"https://www.google.com/travel/flights.com"` with the actual URL of the travel booking website you prefer to use.
6. Execute the script by running the following command in your terminal:
```bash
python flight_search.py
```

## Contact

If you have any questions or need assistance, feel free to contact me at [mirco.macchi@live.it](mailto:mirco.macchi@live.it).
