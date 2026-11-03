# ============================================================
# PS Number      : 80
# Project Title  : Courier Tracking System
# Student Name   : Ajay Kumar Sahu
# Email ID       : Ajay.kumar.sahu@rungta.org
# Section        : BCA 1A
# ============================================================


# Initializing an empty dictionary to store parcel details
parcels = {}


# Defining different stages of parcel delivery
statuses = ["Booked", "Picked Up", "In Transit", "Out for Delivery", "Delivered"]


# Initializing tracking ID counter
count = 1001


# Function to book a new parcel
def book_parcel():
    global count

    # Taking sender, receiver, and destination details
    sender = input("Enter sender name: ")
    receiver = input("Enter receiver name: ")
    destination = input("Enter destination: ")

    # Generating a unique tracking ID
    tid = "CT" + str(count)
    count += 1

    # Storing parcel information in the dictionary
    parcels[tid] = {
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "status": "Booked",
        "history": ["Booked"]
    }

    # Displaying parcel booking confirmation
    print("Parcel booked.")
    print("Tracking ID:", tid)
    print("Status: Booked")


# Function to update parcel delivery status
def update_status():
    # Taking tracking ID from the user
    tid = input("Enter tracking ID: ").upper()

    # Checking whether tracking ID exists
    if tid not in parcels:
        print("Tracking ID", tid, "not found.")
        return

    parcel = parcels[tid]

    # Checking whether parcel is already delivered
    if parcel["status"] == "Delivered":
        print("Parcel already delivered. No further updates allowed.")
        return

    # Updating parcel to the next delivery status
    old = parcel["status"]
    new = statuses[statuses.index(old) + 1]

    parcel["status"] = new
    parcel["history"].append(new)

    # Displaying updated delivery status
    print("Status updated:", old, "->", new)


# Function to track parcel using tracking ID
def track_parcel():
    # Taking tracking ID from the user
    tid = input("Enter tracking ID: ").upper()

    # Checking whether tracking ID exists
    if tid not in parcels:
        print("Tracking ID", tid, "not found.")
        return

    # Retrieving parcel information
    p = parcels[tid]

    # Displaying parcel details and tracking history
    print("Tracking ID:", tid)
    print("Sender:", p["sender"])
    print("Receiver:", p["receiver"])
    print("Destination:", p["destination"])
    print("History:", " -> ".join(p["history"]))
    print("Current status:", p["status"])


# Function to search parcels using receiver name
def search_receiver():
    # Taking receiver name from the user
    name = input("Enter receiver name: ").lower()
    found = False

    # Searching for matching receiver names
    for tid, p in parcels.items():
        if p["receiver"].lower() == name:
            print("Tracking ID:", tid)
            print("Receiver:", p["receiver"])
            print("Destination:", p["destination"])
            print("Status:", p["status"])
            found = True

    # Displaying message if no parcel is found
    if not found:
        print("No parcel found.")


# Main menu of Courier Tracking System
while True:
    print("\n1. Book Parcel")
    print("2. Update Status")
    print("3. Track Parcel")
    print("4. Search by Receiver")
    print("5. Exit")

    # Taking user's menu choice
    choice = input("Enter your choice: ")

    # Option 1: Book a new parcel
    if choice == "1":
        book_parcel()

    # Option 2: Update parcel delivery status
    elif choice == "2":
        update_status()

    # Option 3: Track parcel details
    elif choice == "3":
        track_parcel()

    # Option 4: Search parcel by receiver name
    elif choice == "4":
        search_receiver()

    # Option 5: Exit the application
    elif choice == "5":
        print("Thank you!")
        break

    # Handling invalid menu choices
    else:
        print("Invalid choice.")
