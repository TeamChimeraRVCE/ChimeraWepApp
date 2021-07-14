from firebase import firebase


firebase = firebase.FirebaseApplication(
    "https://chimwebapp-default-rtdb.firebaseio.com/", None
)

toDatabase = {"speed": 60, "temp": 48, "rpm": 2391, "Current": 51.2, "voltage": 518}

battery = {
    "b1": 3.533,
    "b2": 3.542,
    "b3": 3.534,
    "b4": 3.576,
    "b5": 3.584,
    "b6": 3.574,
    "b7": 3.515,
    "b8": 3.578,
    "b9": 3.536,
    "b10": 3.588,
    "b11": 3.529,
    "b12": 3.509,
    "b13": 3.555,
    "b14": 3.586,
    "b15": 3.576,
    "b16": 3.851,
    "b17": 3.509,
    "b18": 3.534,
    "b19": 3.534,
    "b20": 3.576,
    "b21": 3.534,
    "b22": 3.534,
    "b23": 3.527,
    "b24": 3.515,
    "t1": 37.558,
    "t2": 38.016,
    "t3": 37.852,
    "t4": 38.543,
    "t5": 37.690,
    "t6": 37.744,
    "t7": 37.744,
    "t8": 38.570,
    "t9": 37.980,
    "t10": 37.880,
    "t11": 38.121,
    "t12": 38.110,
    "t13": 37.744,
    "t14": 37.591,
    "t15": 38.570,
    "t16": 37.980,
    "t17": 37.880,
    "t18": 37.558,
    "t19": 38.016,
    "t20": 37.852,
    "t21": 38.543,
    "t22": 37.690,
    "t23": 37.744,
    "t24": 37.834,
}

result = firebase.post("/MotorData", toDatabase)
result = firebase.post("/BatteryData", battery)
