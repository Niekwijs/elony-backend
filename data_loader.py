import pandas as pd
import os



class Loader:
    datasets = {}


    def __init__(self):
        self.load_all_in_data()

    def load_all_in_data(self):
        response = {}
        if not os.path.exists('./data'):
            raise FileNotFoundError(f"Folder data not found.")
        
        for filename in os.listdir('./data'):
            if filename.endswith('.csv'):
                    file_path = os.path.join('./data', filename)
                    df = pd.read_csv(file_path)
                    key = os.path.splitext(filename)[0]
                    self.datasets[key] = df

    def get_tesla_stock_range(self, start_date, end_date):
        df_tesla_stock = self.datasets["TSLA ticker 2015 through 2020"]
        df_res = None
        try:
            start_date = pd.to_datetime(start_date).tz_localize('UTC')
            end_date = pd.to_datetime(end_date).tz_localize('UTC')

        except Exception as e:
            print(f'String could not be parsed to datetime:{e}')
            return None
        
        try:
            df_tesla_stock["Date"] = pd.to_datetime(df_tesla_stock["Date"])
            if len(df_tesla_stock) <= 1 :
                print(f"no resuts from date range with { len(df_tesla_stock)}")
        except Exception as e:
            print(f'Parsing Date column went wrong:{e}')
            return None

        try: 
            df_res = df_tesla_stock[(df_tesla_stock['Date']>=start_date) & (df_tesla_stock['Date']<=end_date)]
        except Exception as e:
            print(f'The dates could not be found: {e}')
            return None
        
        return df_res
        

# this is purely for testing purposes
if __name__ == "__main__":
    loader = Loader()

    # Display loaded datasets
    for key, df in loader.datasets.items():
        print(f"Dataset: {key}, Shape: {df.shape}")
    
    df_res = loader.get_tesla_stock_range('2015-01-06 00:00:00+00:00', '2015-04-16 00:00:00+00:00')