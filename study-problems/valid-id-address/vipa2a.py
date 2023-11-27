def validateIP(ip):
  if len(ip) > 16: return False
  numbers_list = ip.split('.')
  if len(numbers_list) != 4: return False
  for num in numbers_list:
    try:
      num_int = int(num) # "12sd3"
      if num_int < 0 or num_int > 255:
        return False
    except:
      return False
  return True


# good job with the comments
# continue?

function fitsOneByte(chunk):
    # Does this string chunk represent a number
    # from 0 to 255?

    # If it's empty string, return false.
    if chunk.length == 0:
        return false

    # If any character in the string isn't a
    # digit, return false.
    for i from 0 to chunk.length - 1:
        if chunk[i] < '0' OR chunk[i] > '9':
            return false

    # If the string has a leading zero and isn't
    # zero, return false.
    if chunk.length >= 2 AND chunk[0] == '0':
        return false

    # Return true if and only if parsing the
    # chunk as an integer is between 0 and 255.
    return 0 <= int(chunk) AND int(chunk) <= 255

function validate(address):
    # If the number of periods is not 3, then
    # it can't be an IP address.
    chunks = address.split('.')
    if chunks.length != 4:
        return false

    # Check that each chunk delimited by periods,
    # represents a number from 0-255.
    for chunk in chunks:
        if not fitsOneByte(chunk):
            return false

    return true
