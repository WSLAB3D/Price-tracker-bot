import schedule
import time
from bot import main  # Adjust to match your bot entrypoint

def run_bot():
    print("[Scheduler] Running bot task...")
    main()

# Schedule to run every hour
schedule.every().hour.at(":00").do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(60)