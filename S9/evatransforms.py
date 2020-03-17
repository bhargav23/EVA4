from torchvision import transforms
class Transforms:

  def test_transforms(self):
    transforms_list = [transforms.ToTensor()]
    return transforms.Compose(transforms_list)

  def train_transforms(self):
    transforms_list = [transforms.ToTensor()]
    return transforms.Compose(transforms_list)