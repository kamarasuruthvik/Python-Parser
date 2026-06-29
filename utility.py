class Utility:
    def increment_count_key(self, key, data):
        if key is None:
            return
        if key not in data:
            data[key] = 1
        else:
            data[key] += 1

