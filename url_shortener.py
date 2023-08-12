import hashlib
def generate_short_url(url):
    # Generate a hash value using a cryptographic hash function
    hash_object = hashlib.md5(url.encode())
    hash_value = hash_object.hexdigest()

    # Select a substring from the hash value to form the short URL
    short_url = hash_value[:8]  # You can change the length as per your requirement

    return short_url
long_url = "https://www.example.com/very/long/url"
short_url = generate_short_url(long_url)
print("Short URL:", short_url)    #generates a short url in hash value