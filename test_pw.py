from playwright.sync_api import sync_playwright
import time

def test_login():
    with sync_playwright() as p:
        browser=p.firefox.launch(headless=False, slow_mo=500)
        page=browser.new_page()
        print("Opening up Login page...")
        page.goto("http://127.0.0.1:5000/login")
        print("Filling information...")
        page.fill("input[name='username']", "Daria")
        page.fill("input[name='password']", "daria1234")
        print("Pressing Login button...")
        page.click("button[type='submit']")
        print("Taking a picture for proof")
        page.screenshot(path="login_proof.png")
        print("Test is done.")
        page.pause()

if __name__=="__main__":
    test_login()