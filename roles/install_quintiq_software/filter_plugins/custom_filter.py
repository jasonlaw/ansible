def is_checksum_contained(checksum, text):
    return checksum.replace('\r\n', '') in text.replace('\r\n', '')

class FilterModule(object):
    def filters(self):
        return {
            'is_checksum_contained': is_checksum_contained,
        }
