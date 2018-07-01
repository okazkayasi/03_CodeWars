# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#
#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59
#
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.

def make_readable(seconds):
    as_minutes = int(seconds / 60)
    secs = seconds - as_minutes * 60
    hrs = int(as_minutes/60)
    mins = as_minutes - hrs * 60
    listed = [str(hrs), str(mins), str(secs)]
    return '{:02}:{:02}:{:02}'.format(hrs, mins, secs)

print make_readable(86399)
