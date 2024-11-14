import requests

classes_url = "https://fireroad.mit.edu/courses/all?full=true"


def get_all_classes():
    response = requests.get(classes_url)
    if response.status_code == 200:
        all_classes_info_raw = response.json()  # list of dicts of len 6585
    else:
        print(f"Failed to fetch all_clases_data: {response.status_code}")

    no_rating = {class_info["subject_id"] for class_info in all_classes_info_raw if "rating" not in class_info}
    no_in_hours = {class_info["subject_id"] for class_info in all_classes_info_raw if "in_class_hours" not in class_info}
    no_out_hours = {class_info["subject_id"] for class_info in all_classes_info_raw if "out_of_class_hours" not in class_info}
    not_public = {class_info["subject_id"] for class_info in all_classes_info_raw if class_info["public"] == False}  # len 0

    bad_data = no_rating.union(no_in_hours).union(no_out_hours).union(not_public)  # len 1882
    all_classes_info = [class_info for class_info in all_classes_info_raw if class_info["subject_id"] not in bad_data]  # len 4703

    return all_classes_info


if __name__=="__main__":
    all_classes = get_all_classes()