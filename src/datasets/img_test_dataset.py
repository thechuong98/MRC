import os

from PIL import Image
from torch.utils.data import Dataset


class TestDataset(Dataset):
    """Example dataset class for loading images from folder."""

    def __init__(self, dir: str, transform):
        self.transform = transform
        self.images = [os.path.join(dir, fname) for fname in os.listdir(dir)]

    def __getitem__(self, idx):
        image = Image.open(self.images[idx]).convert("L")  # convert to black and white
        # image = Image.open(self.images[idx]).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image

    def __len__(self):
        return len(self.images)
