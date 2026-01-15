import requests

class DownloadController:
    def __init__(self, df, download_directory):
        self.df = df
        self.download_directory = download_directory

    def download_files(self):
        for index, row in self.df.iterrows():
            url = row['link_externo']
            filename = row['codigoValidacao']
            dest_path = f"{self.download_directory}/{filename}.pdf"
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(dest_path, 'wb') as file:
                    file.write(response.content)
                print(f"Download completed: {dest_path}")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading file from {url}: {e}")