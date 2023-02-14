import sys

pod_hodinu = [int(x) for x in sys.argv[1:] if int(x) <= 60]

nad_hodinu = [int(x)-60 for x in sys.argv[1:] if int(x) > 60]

print("Do hodiny: " + str(pod_hodinu))
print("Prekroceni o: " + str(nad_hodinu) + " minut")

"""
casy = [12, 25, 64, 27, 15, 66, 128, 44]

pod_hodinu = [x for x in casy if x < 60]

nad_hodinu = [x-60 for x in casy if x > 60]

print(pod_hodinu)
print("Prekroceni o: " + str(nad_hodinu) + " minut")
"""