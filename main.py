import csv
from utility import Utility

class CSVHandler:
    def __init__(self):
        self.logs=  []
        self.user_entries = dict()
        self.log_level_entries = dict()
        self.utility = Utility()
        self.users_with_errors = []



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

                self.logs.append(row_dict)
            


        print(self.logs)




    def count_entries(self):
        for log in self.logs:
            user_name = log['user']
            log_level = log['level']
            self.utility.increment_count_key(user_name, self.user_entries)
            self.utility.increment_count_key(log_level, self.log_level_entries)
            [self.users_with_errors.append(user_name) if log_level == "ERROR" else None]
        

        print(self.user_entries)
        print(self.log_level_entries)
        print(self.users_with_errors)


    def clear_logs(self):
        self.logs.clear()
        self.log_level_entries.clear()
        self.user_entries.clear()
        self.users_with_errors.clear()

csv_handler = CSVHandler()
csv_handler.parse_logs('data.csv')
csv_handler.count_entries()
csv_handler.clear_logs()