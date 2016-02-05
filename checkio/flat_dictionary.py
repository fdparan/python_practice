from pprint import pprint


def combine(dictionary, key_name):

    return dict([('/'.join([key_name, k]),v) \
                 for k, v in dictionary.items()])\
        if len(dictionary) > 0 else {key_name: ""}


def flatten(dictionary):

    stack = [dictionary]
    result = {}
    while stack:

        for k, v in stack.pop().items():
            if isinstance(v, dict):
                stack.append(combine(v, k))
            else:
                result[k] = v

    return result

samp = {"name": {
            "first": "One",
            "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}

print 'Before:'
pprint(samp)

print 'After:'
pprint(flatten(samp))

print flatten({"key": "value"}) == {"key": "value"}, "Simple"
print flatten(
    {"key": {"deeper": {"more": {"enough": "value"}}}}
) == {"key/deeper/more/enough": "value"}, "Nested"
print flatten({"empty": {}}) == {"empty": ""}, "Empty value"
print flatten({"name": {
                    "first": "One",
                    "last": "Drone"},
                "job": "scout",
                "recent": {},
                "additional": {
                    "place": {
                        "zone": "1",
                        "cell": "2"}}}
) == {"name/first": "One",
      "name/last": "Drone",
      "job": "scout",
      "recent": "",
      "additional/place/zone": "1",
      "additional/place/cell": "2"}