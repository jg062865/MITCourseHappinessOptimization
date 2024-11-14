import requests

classes_url = "https://fireroad.mit.edu/courses/all?full=true"
response = requests.get(classes_url)

if response.status_code == 200:
    all_classes_raw = response.json()  # list of dicts of len 6585
else:
    print(f"Failed to fetch all_clases_data: {response.status_code}")

no_rating = {class_info["subject_id"] for class_info in all_classes_raw if "rating" not in class_info}
no_in_hours = {class_info["subject_id"] for class_info in all_classes_raw if "in_class_hours" not in class_info}
no_out_hours = {class_info["subject_id"] for class_info in all_classes_raw if "out_of_class_hours" not in class_info}

bad_data = no_rating.union(no_in_hours).union(no_out_hours)  # len 1882
print(len(bad_data))
all_classes = [class_info for class_info in all_classes_raw if class_info["subject_id"] not in bad_data]  # len 4703
print(len(all_classes)) 

