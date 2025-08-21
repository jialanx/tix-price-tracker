from flask import Flask, request, jsonify, render_template  # FIXED import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price')
def get_price():
    url = request.args.get('url')  # FIXED: now uses Flask's request

    if not url:
        return jsonify(price="Error: No URL provided")

    DRIVER_PATH = 'chromedriver.exe'
    service = Service(DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Make Chrome headless

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        time.sleep(5)
        source = driver.page_source
    except Exception as e:
        return jsonify(price=f"Error: {str(e)}")
    finally:
        try:
            driver.quit()
        except:
            pass

    soup = BeautifulSoup(source, 'lxml')
    content = soup.find('span', {'class': 'MuiTypography-root MuiTypography-body-bold styles_nowrap___p2Eb mui-1nxievo'})
    price = content.text if content else "Not found"
    return jsonify(price=price)

if __name__ == '__main__':
    app.run(debug=True)
