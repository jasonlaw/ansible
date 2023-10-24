def is_checksum_contained(checksum, text):
    return checksum.replace('\r\n', '') in text.replace('\r\n', '')
