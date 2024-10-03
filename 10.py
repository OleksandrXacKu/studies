def new_hashtag(s):
    hashtag = "#" + "".join(word.capitalize() for word in s.split())
    return hashtag if len(hashtag) <= 140 else False
input_string = "я втомився та хочу у відпустку"
print(new_hashtag(input_string))