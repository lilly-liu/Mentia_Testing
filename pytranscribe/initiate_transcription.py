import argparse
import os
import requests


API_URL = "https://api.assemblyai.com/v2/"
CDN_URL = "https://cdn.assemblyai.com/"


def initiate_transcription(file_id):
    """Sends a request to the API to transcribe a specific
    file that was previously uploaded to the API. This will
    not immediately return the transcription because it takes
    a moment for the service to analyze and perform the
    transcription, so there is a different function to retrieve
    the results.
    """
    custom = ["Julie", "Robin", "Livingroom", "Bedroom", "Bathroom", "Garden", "Barn", "tackroom", "drink", "tap", "follow", "books", "movies", "sport", "travel", "fire", "light", "records", "door", "records", "painting", "piano", "window", "music", "song", "tune", "chocolates", "fan", "outfit", "closet", "bed", "carpet", "TV", "television", "cat", "couch", "recliner", "seat", "lamp", "pillows", "blankets", "clothing", "hat", "sunglasses", "medication", "pill", "music", "teeth", "brush", "pajamas", "sleep", "freshen", "clean", "toothpaste", "gums", "heater", "bathrobe", "shower", "curtain", "toilet", "washcloth", "cream", "moisturize", "nail", "polish", "deodorant", "perfume", "lipstick", "powder", "pencil", "eyebrows", "blow", "dryer", "drawer", "shaving", "shave", "razor", "comb", "scale", "mirror", "sink", "water", "flower", "carrot", "vegetables", "dirt", "plants", "lettuce", "tomato", "tomatoes", "tree", "sun", "sunny", "birdbath", "bird", "bucket", "apple", "kitty", "shade", "radio", "barn", "stall", "starr", "grooming", "groom", "horse", "work", "dixie", "pasture", "touch", "dirt", "fur", "curry", "comb", "coat", "mane", "shine", "body", "face", "halter", "rope", "strokes", "fred", "dog", "rosie", "goat", "gate"]
    endpoint = "".join([API_URL, "transcript"])
    json = {"audio_url": "".join([CDN_URL, "upload/{}".format(file_id)]), "disfluencies": True,
    "word_boost": custom}
    headers = {
        "authorization": os.getenv("ASSEMBLYAI_KEY"),
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_id")
    args = parser.parse_args()
    file_id = args.file_id
    response_json = initiate_transcription(file_id)
    print(response_json)
