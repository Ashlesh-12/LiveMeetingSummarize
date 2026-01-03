#simple transaction data(amount, location)
transactions=[
    (2000,"local"),
    (50,"local"),
    (1000,"local"),
    (500,"foreign"),
    (200,"local")
    ]
# define thresolds
MAX_NORMAL_AMOUNT=1000
ALLOWED_LOCATIONS=["local"]
def defect_anomalies(transactions):
    anomalies=[]
    for idx,(amount, location) in enumerate(transactions,start=1):
        if amount>MAX_NORMAL_AMOUNT or location not in ALLOWED_LOCATIONS:
            anomalies.append({
                "transaction_id":idx,
                "amount":amount,
                "location":location,
                "reason":"High Amount" if amount>MAX_NORMAL_AMOUNT else "Unusal Location"
            })
    return anomalies
anomalies=defect_anomalies(transactions)
if anomalies:
    print("Suspicious Transactions Detected:")
    for anomaly in anomalies:
        print(f"ID {anomaly['transaction_id']}: Amount={anomaly['amount']}, Location={anomaly['location']}, Reason={anomaly['reason']}")
else:
    print("No suspicious transactions detected.")

