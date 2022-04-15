# Hosting Options
* Google Cloud
  * Cloud Run - expensive with always-on CPU
  * Compute Engine - free micro instance is enough. Not as fancy CD pipeline though.
     * https://cloud.google.com/blog/topics/developers-practitioners/build-and-run-discord-bot-top-google-cloud
     * https://cloud.google.com/compute/docs/containers/deploying-containers
* Heroku
  * https://medium.com/@linda0511ny/create-host-a-discord-bot-with-heroku-in-5-min-5cb0830d0ff2
  * 1000 free dyno hours per month, covers Always on 24/7 https://devcenter.heroku.com/articles/free-dyno-hours However will compete agains other apps hosted there
* https://vercel.com/pricing
* https://www.techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/
* https://alaister.net/
* https://www.pythonanywhere.com
* https://www.reddit.com/r/Discord_Bots/comments/mtjr27/any_new_free_discord_bot_free_247_hosting/
* Raspberrypi https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
  * Set up dyndns with Cloudflare, then scp action to deploy?

