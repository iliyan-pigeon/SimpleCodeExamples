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


def compare_faces(first_image, second_image):
    tolerance = 0.6

    first_image_encoding = face_recognition.face_encodings(first_image)[0]
    second_image_encoding = face_recognition.face_encodings(second_image)[0]

    result = face_recognition.compare_faces([first_image_encoding], second_image_encoding, tolerance)[0]
    face_distance = face_recognition.face_distance([first_image_encoding], second_image_encoding)[0]
    similarity_percentage = (1.0 - face_distance) * 100

    return result, face_distance, similarity_percentage
