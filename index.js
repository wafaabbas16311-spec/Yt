const puppeteer = require('puppeteer');

async function runViews() {
    // 1. Launch the browser
    const browser = await puppeteer.launch({ 
        headless: true, // Set to false if you want to see the browser window
        args: ['--no-sandbox', '--disable-setuid-sandbox'] 
    });
    const page = await browser.newPage();

    // REPLACE this URL with your actual YouTube video link
    const videoUrl = 'https://youtube.com/shorts/EiU2ueuFed0?si=tfWufSSgi4lbNYVW';

    console.log(`Navigating to ${videoUrl}...`);
    await page.goto(videoUrl);

    // Click the video to play it (sometimes it starts as a preview)
    await page.click('button.ytp-play-button'); 

    // Logic to keep it running until 100 hours
    // We use a loop that refreshes or simply lets the video loop
    let totalWatchTimeMinutes = 0;
    const viewDurationMinutes = 5; // Average length of your video or loop de-facto

    while (totalWatchTimeMinutes < 6000) { // 6000 minutes = 100 hours
        console.log(`Current watch time: ${totalWatchTimeMinutes} minutes`);
        
        // Wait for the duration of one view (or use a timer)
        await new Promise(resolve => setTimeout(resolve, viewDurationMinutes * 60000));
        
        // Refresh the page to count a new view, or just let it loop de-facto
        await page.reload(); 
        totalWatchTimeMinutes += viewDurationMinutes;
    }

    await browser.close();
}

runViews().catch(err => console.error("Error running views:", err));
