import face_recognition
import face_recognition_models


def find_face_location(image_path):
    model = "hog"

    image = face_recognition.load_image_file(f"{image_path}")
    location = face_recognition.face_locations(image, model=model)

    if location:
        return location
    else:
        return None


def compare_faces(first_image, first_face_location, second_image, second_face_location):
    tolerance = 0.6

    image_one = face_recognition.load_image_file(f"{first_image}")
    image_two = face_recognition.load_image_file(f"{second_image}")

    first_image_encoding = face_recognition.face_encodings(image_one, first_face_location)[0]
    second_image_encoding = face_recognition.face_encodings(image_two, second_face_location)[0]

    result = face_recognition.compare_faces([first_image_encoding], second_image_encoding, tolerance)[0]
    face_distance = face_recognition.face_distance([first_image_encoding], second_image_encoding)[0]

    return result, face_distance





