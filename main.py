PROMISED_DOWN = 150
PROMISED_UP = 10
# CHROME_DRIVER_PATH = "/C:/Users/surya/"

TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

from Bot import InternetSpeedTwitterBot

I = InternetSpeedTwitterBot()
I.get_internet_speed(PROMISED_DOWN, PROMISED_UP)

I.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)