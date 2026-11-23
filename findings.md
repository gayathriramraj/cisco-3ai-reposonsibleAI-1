# Responsible-use review: three AI-generated samples
 
| Sample | Item failed | Finding and action |
|---|---|---|
| 1 - get_weather() | Verified | requests.get_json does not exist (AttributeError). Replaced with requests.get(url, timeout=10).json() after checking the library. |
| 2 - merge_sort() | Licensed | Generated to match a GPL-licensed source. Replaced with sorted(); hold any similar code for a license review. |
| 3 - stack trace prompt | Clean of secrets | An API key was in the prompt draft. Redacted before sending; rotate any key that has already been sent
