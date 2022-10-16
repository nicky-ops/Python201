courses = {
    "ETI 2201": "Analog Electronics",
    "ETI 2202": "Power Electronics",
    "ETI 2203": "Digital Electronics",
    "ETI 2204": "Instrumentation and Measurements"
}
unit = courses.get("ETI 2201", None)
if courses.get("ETI 2201",None):
    print(f"You are enrolled in {unit}")
