# Amazon Price Tracker 📉📧

This Python program enables users to track the pricing of a product on the Amazon website over a period of time. If the price drops below the user's desired amount, it sends a Gmail notification containing the product link, facilitating immediate purchase.

## Features

- **Price Tracking:** Continuously monitors the price of a specified product on Amazon.
- **Price Drop Notification:** Sends a Gmail notification when the price falls below the user's specified threshold.
- **Product Link:** Includes the direct link to the product in the notification for quick access.
- **Easy Setup:** Simple to configure and use with minimal dependencies.

## Libraries Used

- **Beautiful Soup:** For web scraping to extract product information from Amazon's website.
- **Requests:** To send HTTP requests and retrieve web pages.
- **SMTP:** For sending email notifications.
- **Time:** For implementing time delays and scheduling tasks.

## How to Use

1. **Installation:** Install the required libraries using pip:
    ```
    pip install beautifulsoup4 requests
    ```

2. **Setup Gmail:** Enable less secure apps in your Gmail settings to allow sending emails via SMTP. Note: This might pose security risks, so exercise caution.

3. **Configuration:** Modify the script to include your Gmail credentials, desired product URL, and target price.

4. **Run the Script:** Execute the Python script and let it run in the background. It will periodically check the price and notify you via email when it drops below your specified amount.

## Example

```python
python price.py

