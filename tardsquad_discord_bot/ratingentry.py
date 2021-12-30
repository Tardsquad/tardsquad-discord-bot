from datetime import datetime, timedelta

RATING_EXPIRES_AFTER_H = 6


class RatingEntry:
    def __init__(self, user, rating, reason=None):
        self.user = user
        self.rating = rating
        self.reason = reason
        self.expiry_time = datetime.now() + timedelta(hours=RATING_EXPIRES_AFTER_H)
        # For testing:
        # self.expiry_time = datetime.now() + timedelta(minutes=2)

    def expires_at(self):
        now = datetime.now()
        diff = self.expiry_time - now
        if diff.total_seconds() < 0:
            return "now"
        else:
            hours, rem = divmod(diff.seconds, 3600)
            minutes, _ = divmod(rem, 60)
            return "{:d}h{:d}m".format(hours, minutes)

    def expired(self):
        now = datetime.now()
        diff = self.expiry_time - now
        return diff.total_seconds() < 0
