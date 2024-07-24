def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Avengers", power="High")

print_kwargs(name="Avengers", power="High", enemy="Thanos")
