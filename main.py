import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- CONFIGURATION ---
VIDEO_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" # Replace with your URL
TARGET_HOURS = 100 
# 100 hours = 6,000 minutes = 360,000 seconds
# If you have 1 browser tab, it takes 360k seconds. 
# If you run multiple tabs, it's faster.
TOTAL_SECONDS_NEEDED = TARGET_HOURS * 3600 

def run_youtube_bot():
    # Setup Chrome options for Railway (Headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Runs without a GUI (essential for Railway)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    print(f"Navigating to {VIDEO_URL}...")
    driver.get(VIDEO_URL)
    
    # Mute the video so it doesn't crash the server with sound
    # This clicks the mute button or uses JS to mute
    driver.execute_script("document.querySelector('video').muted = true")
    
    start_time = time.time()
    elapsed_time = 0
    
    while elapsed_time < TOTAL_SECONDS_NEEDED:
        # Refresh every 30 minutes to prevent the video from ending 
        # (if it's a short video) or just let it loop in a playlist
        time.sleep(60) # Check every minute
        elapsed_time = time.time() - start_time
        
        # Optional: Every 30 mins, refresh the page to count a new view
        if int(elapsed_time) % 1800 == 0:
            driver.refresh()
            print("Page refreshed for a new view...")

    print(f"Reached {TARGET_HOURS} hours of watch time!")
    driver.quit()

if __name__ == "__main__":
    run_youtube_bot()
