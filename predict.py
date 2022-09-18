import numpy as np
from cog import BasePredictor, Input, Path
from PIL import Image
import torch
from torchvision.models import resnet18

class Predictor(BasePredictor):
    def setup(self):
        self.model = resnet18(pretrained=True)
        model.fc = torch.nn.Sequential(model.fc, torch.nn.Softmax(dim=1))

    @torch.inference_mode()
    @torch.cuda.amp.autocast()
    def predict(self, image: Path = Input(description="Image to classify")) -> int:
        img = Image.open(str(image)).convert('RGB')
        img = preprocess_input(img)
        preds = self.model(img)

        return torch.argmax(preds)

    def preprocess_input(self, img):
        img = np.asarray(img).astype(np.float32)
        img = torch.tensor(img)
        img = torch.permute(img, (2, 0, 1))
        img = img.unsqueeze(0)

        return img
