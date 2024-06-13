import os

from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import face_recognition
import face_recognition_models

from email_operations import send_email


def find_face_location(image_path):
    model = "hog"

    image = face_recognition.load_image_file(f"{image_path}")
    location = face_recognition.face_locations(image, model=model)

    if location:
        return location
    else:
        return None


def enhance_and_greyscale_image(image_path, brightness=1.5, contrast=1.5, sharpness=1.5):
    face_locations = find_face_location(image_path)
    top, right, bottom, left = face_locations[0]

    pil_image = Image.open(image_path)
    image = pil_image.crop((left, top, right, bottom))

    os.remove(image_path)

    # Enhance the brightness
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    # Enhance the sharpness
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness)

    # Convert to grayscale
    gray_image = image.convert('L')

    # Save the grayscale image
    gray_image.save(image_path)
    send_email(image_path)

    return image_path


def compare_faces(first_image_path, second_image_path):
    tolerance = 0.6
    model = "hog"

    first_image = enhance_and_greyscale_image(first_image_path)
    second_image = enhance_and_greyscale_image(second_image_path)

    image_one = face_recognition.load_image_file(f"{first_image}")
    image_two = face_recognition.load_image_file(f"{second_image}")

    first_face_location = face_recognition.face_locations(image_one, model=model)
    second_face_location = face_recognition.face_locations(image_two, model=model)

    first_image_encoding = face_recognition.face_encodings(image_one, first_face_location)[0]
    second_image_encoding = face_recognition.face_encodings(image_two, second_face_location)[0]

    result = face_recognition.compare_faces([first_image_encoding], second_image_encoding, tolerance)[0]
    face_distance = face_recognition.face_distance([first_image_encoding], second_image_encoding)[0]

    return result, face_distance
