# Courier Tracking System

| Detail | Info |
|---|---|
| **PS Number** | 80 |
| **Student Name** | Ajay Kumar Sahu |
| **Email ID** | Ajay.kumar.sahu@rungta.org |
| **Section** | BCA 1A |
| **ERP No** | 01235 |

## Project Overview
Courier Tracking System ek console-based Python program hai jisse courier parcels ko book, update, track aur search kiya ja sakta hai. Sabhi parcel details Python dictionary mein store hoti hain.

## Objectives
- Parcel booking process ko automate karna.
- Har parcel ko unique Tracking ID dena.
- Parcel ke delivery stages ko step-by-step update karna.
- Tracking ID ya receiver name se parcel ki jaankari nikalna.

## Features
1. **Book Parcel**: Sender, receiver aur destination lekar unique Tracking ID (CT1001, CT1002, ...) banata hai.
2. **Update Status**: Status agle stage par le jata hai:
   Booked -> Picked Up -> In Transit -> Out for Delivery -> Delivered
3. **Track Parcel**: Parcel ki poori details, history aur current status dikhata hai.
4. **Search by Receiver**: Receiver ke naam se parcels dhoondta hai (case-insensitive).
5. **Exit**: Program band karta hai.

Extra: Tracking ID case-insensitive hai (ct1001 bhi chalega), galat ID aur galat menu choice handle hoti hai, aur "Delivered" ke baad update nahi hota.

## Requirements
- Python 3.x
- Koi external library zaroori nahi.

## How to Run
```
python one.py
```

## Input / Output Details
**Input:** Menu choice (1-5), sender, receiver, destination, Tracking ID, receiver name.

**Output:** Booking confirmation, status update message, tracking details, search results.

## Test Cases

| # | Test Case | Input | Expected Output |
|---|---|---|---|
| 1 | Book parcel | 1, Ram, Shyam, Raipur | Parcel booked. Tracking ID: CT1001. Status: Booked |
| 2 | Update status | 2, CT1001 | Status updated: Booked -> Picked Up |
| 3 | Update status (lowercase ID) | 2, ct1001 | Status updated: Picked Up -> In Transit |
| 4 | Track parcel | 3, CT1001 | Sender, Receiver, Destination, History, Current status |
| 5 | Search by receiver (found) | 4, shyam | Tracking ID, Receiver, Destination, Status |
| 6 | Search by receiver (not found) | 4, xyz | No parcel found. |
| 7 | Track invalid ID | 3, CT9999 | Tracking ID CT9999 not found. |
| 8 | Update invalid ID | 2, CT9999 | Tracking ID CT9999 not found. |
| 9 | Update after delivered | 2, CT1001 (status Delivered) | Parcel already delivered. No further updates allowed. |
| 10 | Invalid menu choice | 9 | Invalid choice. |
| 11 | Exit | 5 | Thank you! |

## Files
- one.py: Complete project code
- README.md: Project documentation
- Screenshots.pdf: Input/output screenshots of all test cases
