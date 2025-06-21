blacklisted_domains = {"fraud.net", "scammer.org", "phishy.biz"}


def is_blacklisted(email: str) -> bool:
    domain = email.split("@")[-1].lower()
    return domain in blacklisted_domains
