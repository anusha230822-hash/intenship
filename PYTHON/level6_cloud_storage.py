from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload(self, filename):
        pass

    @abstractmethod
    def download(self, filename):
        pass

class GoogleDrive(CloudStorage):
    def upload(self, filename):
        return f"Uploaded {filename} to Google Drive"
    def download(self, filename):
        return f"Downloaded {filename} from Google Drive"

class AWSStorage(CloudStorage):
    def upload(self, filename):
        return f"Uploaded {filename} to AWS S3"
    def download(self, filename):
        return f"Downloaded {filename} from AWS S3"

class AzureStorage(CloudStorage):
    def upload(self, filename):
        return f"Uploaded {filename} to Azure Blob"
    def download(self, filename):
        return f"Downloaded {filename} from Azure Blob"

if __name__ == '__main__':
    stores = [GoogleDrive(), AWSStorage(), AzureStorage()]
    for s in stores:
        print(s.upload('file.txt'))
        print(s.download('file.txt'))
