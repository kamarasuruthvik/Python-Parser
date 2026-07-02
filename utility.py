import datetime

class Utility:
    def increment_count_key(self, key, data):
        if key is None:
            return
        if key not in data:
            data[key] = 1
        else:
            data[key] += 1

    def convert_hh_mm_ss_to_hh_mm(self, timestamp):
        timestamp_arr = timestamp.split(":")
        hour = timestamp_arr[0]
        minute = timestamp_arr[1]
        return ":".join([hour, minute])
        

