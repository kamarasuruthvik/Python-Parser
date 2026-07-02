import csv
from utility import Utility

class CSVHandler:
    def __init__(self):
        self.user_entries = dict()
        self.log_level_entries = dict()
        self.utility = Utility()
        self.users_with_errors = dict()
        self.error_minutes = dict()


    def parse_logs(self, filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                row_dict = dict(zip(header, row))

                # Normalize missing values
                for key in row_dict:
                    if row_dict[key] == "":
                        row_dict[key] = None
                
                # Perform Aggregation

                user_name = row_dict.get("user")
                log_level = row_dict.get("level")
                timestamp = row_dict.get("time")
                timestamp_minute_rounded = self.utility.convert_hh_mm_ss_to_hh_mm(timestamp)



                self.utility.increment_count_key(user_name, self.user_entries) # user entries
                self.utility.increment_count_key(log_level, self.log_level_entries) # log level entries
                if log_level == "ERROR":
                    if user_name is not None:
                        self.utility.increment_count_key(user_name, self.users_with_errors)
                    self.utility.increment_count_key(timestamp_minute_rounded, self.error_minutes) # minutes with errors
                




        print(self.users_with_errors)
        print(self.log_level_entries)
        print(self.user_entries)
        print(self.error_minutes)


    def detect_spikes(self):
        spikes = []
        for minute, errors in self.error_minutes.items():
            if errors >= 2:
                spikes.append(minute)

        return spikes

    def detect_top_two_errored_users(self):
        return sorted(self.users_with_errors.items(), key= lambda x: x[1], reverse=True)[:2]



    def clear_logs(self):
        self.log_level_entries.clear()
        self.user_entries.clear()
        self.users_with_errors.clear()
        self.error_minutes.clear()

csv_handler = CSVHandler()
csv_handler.parse_logs('data.csv')
print(csv_handler.detect_spikes())
print(csv_handler.detect_top_two_errored_users())
csv_handler.clear_logs()