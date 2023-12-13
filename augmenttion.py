import os
import random
import string
import cv2
import secrets

def data_augmentation(input_dir, output_dir):

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  for file in os.listdir(input_dir):
    image = cv2.imread(os.path.join(input_dir, file))

    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("augmented_images/" + generate_hash() + ".jpg" , image)

    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite("augmented_images/" + generate_hash() + ".jpg" , image)

def generate_hash():

    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(caracteres) for _ in range(5))

if __name__ == "__main__":
  input_dir = "new"
  output_dir = "augmented_images"

  data_augmentation(input_dir, output_dir)

