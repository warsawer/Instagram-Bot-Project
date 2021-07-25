from instapy import InstaPy
session = InstaPy(username="dughorg", password="Tekos2017")
session.login()
session.like_by_tags(["bmw", "mersedes"], amount=5) # [1]
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_do_comment(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()

# quotas
session.set_quota_supervisor(enabled=True, peak_likes_daily=240, peak_likes_hourly=21)

# for server, without graphical user interface
session = InstaPy(username='test', password='test', headless_browser=True)

# artificial intelligence for the messages analysis
session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
session.clarifai_check_img_for(['nsfw'])

# subscribers amount

session.set_relationship_bounds(enabled=True, max_followers=10000)